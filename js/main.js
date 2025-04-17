// Dados dos projetos
const projects = [
  {
    id: "project1",
    title: "E-commerce com React",
    description:
      "Um site completo de e-commerce desenvolvido com React, incluindo carrinho de compras funcional, sistema de filtros e integração com API de pagamentos.",
    shortDescription: "E-commerce completo com React e API de pagamentos",
    image: "assets/images/project1.jpg",
    tags: ["React", "JavaScript", "API REST", "CSS"],
    repoUrl: "https://github.com/seu-usuario/ecommerce-react",
    demoUrl: "https://seu-ecommerce.netlify.app",
    iframeUrl: "https://seu-ecommerce.netlify.app",
  },
  {
    id: "project2",
    title: "Todo App com Vue.js",
    description:
      "Aplicativo de gerenciamento de tarefas desenvolvido com Vue.js e Vuex para gerenciamento de estado. Inclui funcionalidades de adicionar, editar, excluir tarefas e marcar como concluídas.",
    shortDescription: "Aplicativo de gerenciamento de tarefas com Vue.js",
    image: "assets/images/project2.jpg",
    tags: ["Vue.js", "Vuex", "JavaScript", "CSS"],
    repoUrl: "https://github.com/seu-usuario/todo-vue",
    demoUrl: "https://seu-todo.netlify.app",
    iframeUrl: "https://seu-todo.netlify.app",
  },
  {
    id: "project3",
    title: "Blog em Next.js",
    description:
      "Blog pessoal desenvolvido com Next.js e Markdown para conteúdo. Inclui sistema de categorias, pesquisa e comentários.",
    shortDescription: "Blog pessoal com Next.js e Markdown",
    image: "assets/images/project3.jpg",
    tags: ["Next.js", "React", "Markdown", "CSS Modules"],
    repoUrl: "https://github.com/seu-usuario/blog-nextjs",
    demoUrl: "https://seu-blog.vercel.app",
    iframeUrl: "https://seu-blog.vercel.app",
  },
  {
    id: "project4",
    title: "Dashboard Administrativo",
    description:
      "Dashboard administrativo com gráficos interativos, tabelas de dados e controle de usuários. Desenvolvido com React e Material UI.",
    shortDescription: "Dashboard administrativo com React e Material UI",
    image: "assets/images/project4.jpg",
    tags: ["React", "Material UI", "Chart.js", "Context API"],
    repoUrl: "https://github.com/seu-usuario/admin-dashboard",
    demoUrl: "https://seu-dashboard.netlify.app",
    iframeUrl: "https://seu-dashboard.netlify.app",
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
