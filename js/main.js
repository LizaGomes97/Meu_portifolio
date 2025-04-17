// Dados dos projetos
const projects = [
  {
    id: "processador-de-orcamentos",
    title: "Processador de orçamentos",
    description:
      "Aplicação desenvolvida para converter dados brutos do carrinho de compras do cliente em um orçamento pronto para a impressão",
    shortDescription: "Conversor de dados brutos em orçamento estruturado",
    image: "assets/images/project1.png",
    tags: ["HTML", "JavaScript", "Python", "CSS"],
    repoUrl: "https://github.com/LizaGomes97/Gerador_de_orcamentos",
    demoUrl:
      "https://gerador-de-orcamentos-git-main-lizagomes97s-projects.vercel.app/",
    iframeUrl:
      "https://gerador-de-orcamentos-git-main-lizagomes97s-projects.vercel.app/",
  },
  {
    id: "compre-seu-ingresso",
    title: "Alura - Compre seu ingresso",
    description: "Aplicação desenvolvida para estudos de logica de programação",
    shortDescription: "Compre seus ingressos enquanto estão disponiveis",
    image: "assets/images/compre-ingressos.png",
    tags: ["JavaScript"],
    repoUrl:
      "https://github.com/LizaGomes97/Praticando_Logica/tree/main/ingresso",
    demoUrl: "https://compra-de-ingressos-beta.vercel.app/",
    iframeUrl: "https://compra-de-ingressos-beta.vercel.app/",
  },
  {
    id: "alugames",
    title: "Alura - Alugames",
    description:
      "Aplicação desenvolvida para fins de estudos de logica de programação",
    shortDescription: "Alugue ou devolva filmes conforme disponibilidade",
    image: "assets/images/alugames.png",
    tags: ["Next.js", "React", "Markdown", "CSS Modules"],
    repoUrl:
      "https://github.com/LizaGomes97/Praticando_Logica/tree/main/alugames",
    demoUrl: "https://aluguel-de-jogos-coral.vercel.app/",
    iframeUrl: "https://aluguel-de-jogos-coral.vercel.app/",
  },
  {
    id: "amigo-secreto",
    title: "Alura - Amigo Secreto",
    description: "Jogo de sorteio do amigo secreto",
    shortDescription:
      "Digite o nome de alguns amigos e sorteie quem vai presentear quem",
    image: "assets/images/amigo-secreto.png",
    tags: ["JavaScript"],
    repoUrl:
      "https://github.com/LizaGomes97/Praticando_Logica/tree/main/amigo-secreto",
    demoUrl: "https://amigo-secreto-six-mu.vercel.app/",
    iframeUrl: "https://amigo-secreto-six-mu.vercel.app/",
  },
  {
    id: "carrinho-de-compras",
    title: "Alura - Amigo Secreto",
    description: "Jogo de sorteio do amigo secreto",
    shortDescription:
      "Digite o nome de alguns amigos e sorteie quem vai presentear quem",
    image: "assets/images/carrinho-de-compras.png",
    tags: ["JavaScript"],
    repoUrl:
      "https://github.com/LizaGomes97/Praticando_Logica/tree/main/carrinho-compras",
    demoUrl: "https://carrinhodecompras-eight.vercel.app/",
    iframeUrl: "https://carrinhodecompras-eight.vercel.app/",
  },
  {
    id: "adivinha-numeros-com-narrador",
    title: "Alura - Adivinhe o numero secreto (com narrador)",
    description: "Adivinhe o numero secreto",
    shortDescription: "Adivinhe o numero secreto",
    image: "assets/images/adivinhe-o-numero-secreto.png",
    tags: ["JavaScript"],
    repoUrl:
      "https://github.com/LizaGomes97/Praticando_Logica/tree/main/sorteador-numeros",
    demoUrl: "https://jogo-ashen-psi.vercel.app/",
    iframeUrl: "https://jogo-ashen-psi.vercel.app/",
  },
];

// Função para renderizar a página inicial
function renderHomePage() {
  const template = document
    .getElementById("home-template")
    .content.cloneNode(true);
  const projectsGrid = template.querySelector("#projectsGrid");

  projects.forEach((project) => {
    const projectCard = document.createElement("div");
    projectCard.className = "project-card";
    projectCard.innerHTML = `
            <img src="${project.image}" alt="${
      project.title
    }" class="project-img">
            <div class="project-info">
                <h3>${project.title}</h3>
                <p>${project.shortDescription}</p>
                <div class="project-tags">
                    ${project.tags
                      .slice(0, 3)
                      .map((tag) => `<span class="tag">${tag}</span>`)
                      .join("")}
                </div>
                <a href="#project/${project.id}" class="btn">Ver Detalhes</a>
            </div>
        `;
    projectsGrid.appendChild(projectCard);
  });

  return template;
}

// Função para renderizar a página do projeto
function renderProjectPage(projectId) {
  const project = projects.find((p) => p.id === projectId);
  if (!project) return null;

  const template = document
    .getElementById("project-template")
    .content.cloneNode(true);

  template.querySelector("#projectTitle").textContent = project.title;
  template.querySelector("#projectDescription").textContent =
    project.description;
  template.querySelector("#repoLink").href = project.repoUrl;
  template.querySelector("#demoLink").href = project.demoUrl;
  template.querySelector("#projectIframe").src = project.iframeUrl;

  const tagsContainer = template.querySelector("#projectTags");
  project.tags.forEach((tag) => {
    const tagSpan = document.createElement("span");
    tagSpan.className = "tag";
    tagSpan.textContent = tag;
    tagsContainer.appendChild(tagSpan);
  });

  return template;
}

// Função para renderizar a página de currículo
function renderCurriculumPage() {
  const template = document
    .getElementById("curriculum-template")
    .content.cloneNode(true);
  return template;
}

// Função para lidar com a navegação
function handleNavigation() {
  const pageContent = document.getElementById("pageContent");
  const hash = window.location.hash || "#home";
  pageContent.innerHTML = "";

  if (hash === "#home" || hash === "") {
    pageContent.appendChild(renderHomePage());
  } else if (hash.startsWith("#project/")) {
    const projectId = hash.replace("#project/", "");
    const projectContent = renderProjectPage(projectId);
    if (projectContent) {
      pageContent.appendChild(projectContent);
    } else {
      window.location.hash = "#home";
    }
  } else if (hash === "#curriculum") {
    pageContent.appendChild(renderCurriculumPage());
  }
}

// Lidar com o menu mobile
document.getElementById("hamburger").addEventListener("click", function () {
  document.getElementById("navLinks").classList.toggle("active");
});

// Inicializar a navegação
window.addEventListener("hashchange", handleNavigation);
document.addEventListener("DOMContentLoaded", handleNavigation);
