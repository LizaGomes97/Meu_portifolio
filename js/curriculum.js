// Dados do currículo
const curriculumData = {
  // Informações pessoais
  personalInfo: {
    name: "Lizandra Ribeiro Gomes Placido dos Santos",
    title: "Desenvolvedora de Software | Automação de processos",
    email: "lizandraplacido@gmail.com",
    phone: "(11) 91595-9763",
    location: "Guanambi, Bahia, Brasil",
    linkedin: "www.linkedin.com/in/lizandra-ribeiro-p-santos",
    github: "https://github.com/LizaGomes97",
    about:
      "Desenvolvedora de soluções que visam aumentar a eficiência dos processos e reduzir o tempo gasto com atividades repetitivas no dia-a-dia, permitindo dar foco no que é realmente necessário para o crescimento da empresa. Combinando minha experiência operacional com minhas habilidades em programação, ofereço soluções inovadoras e condizentes com o atual cenário tecnológico do mercado.",
    availability: "Disponível para trabalho remoto ou mudança",
    interests: [
      "OpenToWork",
      "DEV",
      "IA",
      "AWS",
      "MachineLearnig",
      "Python",
      "JavaScript",
      "Liderança",
      "Back-End",
    ],
  },

  // Experiência Profissional
  experience: [
    {
      id: "exp1",
      position: "Desenvolvedor de software",
      company: "Autônomo",
      period: "Janeiro 2024 - Presente",
      description:
        "Desenvolvimento de soluções tecnológicas personalizadas para clientes diversos, com foco em automação e processamento de dados.",
      responsibilities: [
        "Desenvolvimento de ChatBot para WhatsApp: Arquitetura e implementação de solução de atendimento automatizado com Node.js/Jest, reduzindo o tempo de resposta ao cliente e melhorando a satisfação do usuário",
        "Gerador de Orçamentos: Transformação de processo manual de 5-10 minutos em solução automatizada com Python, reduzindo tempo de execução para menos de 1 minuto e aumentando a precisão dos orçamentos",
      ],
      technologies: [
        "Node.js",
        "JavaScript",
        "Python",
        "React Native",
        "APIs",
        "Automação",
      ],
    },
    {
      id: "exp2",
      position: "Supervisora Expansionista",
      company: "RD Saúde",
      period: "Dezembro 2023 - Presente",
      location: "Guanambi, Bahia, Brasil",
      description:
        "Liderança de equipes e implementação de melhorias em processos com uso de dados e tecnologia.",
      responsibilities: [
        "Implementação de metodologias ágeis de treinamento, utilizando análise de dados para identificar padrões e áreas prioritárias de desenvolvimento",
        "Utilização inteligente de dados do Power BI para tomada de decisões estratégicas",
        "Automação de processos com Forms e Excel",
        "Criação e execução de programa de mentoria estruturado para novos colaboradores",
        "Implementação de soluções digitais que modernizaram processos",
        "Utilização de Microsoft Copilot e ferramentas de IA para análise preditiva de métricas de desempenho",
      ],
      technologies: [
        "Metodologias ágeis (Scrum/Kanban)",
        "Análise de dados",
        "Power BI",
        "Automação de processos",
        "Microsoft 365",
        "Liderança",
      ],
    },
    {
      id: "exp3",
      position: "Balconista",
      company: "RD Saúde",
      period: "Novembro 2022 - Dezembro 2023",
      location: "Xangri-lá, Rio Grande do Sul, Brasil",
      //   description:
      // "Atendimento ao cliente e conhecimento das leis que regem a dispensação de antibióticos e psicotrópicos.",
    },
    {
      id: "exp4",
      position: "Caixa",
      company: "RD Saúde",
      period: "Março 2022 - Outubro 2022",
      location: "Capão da Canoa, Rio Grande do Sul, Brasil",
      //   description: "Atendimento ao cliente e operações de caixa.",
    },
    {
      id: "exp5",
      position: "Caixa de atendimento ao cliente",
      company: "Pastello SSA",
      period: "Março 2018 - Setembro 2019",
      location: "Salvador, Bahia, Brasil",
      //   description: "Atendimento ao cliente e operações de caixa.",
    },
  ],

  // Educação
  education: [
    {
      id: "edu1",
      degree: "Bacharelado em Ciência da Computação",
      institution: "Anhanguera Educacional",
      period: "Janeiro 2023 - Julho 2026 (Previsão)",
      description:
        "Formação em andamento com foco em algoritmos, estruturas de dados, banco de dados e programação orientada a objetos.",
    },
  ],

  // Habilidades técnicas
  technicalSkills: [
    { name: "Python", level: "Intermediário" },
    { name: "JavaScript", level: "Intermediário" },
    { name: "HTML/CSS", level: "Intermediário" },
    { name: "Node.js", level: "Intermediário" },
    { name: "React/React Native", level: "Intermediário" },
    { name: "Git/GitHub", level: "Intermediário" },
    { name: "SQL (MySQL)", level: "Intermediário" },
    { name: "Power BI", level: "Intermediário" },
    { name: "Automação de Processos", level: "Avançado" },
    { name: "AWS", level: "Básico" },
    { name: "Machine Learning", level: "Básico" },
    { name: "APIs RESTful", level: "Básico" },
  ],

  // Soft Skills
  softSkills: [
    "Liderança",
    "Pensamento inovador",
    "Trabalho em equipe",
    "Comunicação eficaz",
    "Resolução de problemas",
    "Aprendizado contínuo",
    "Adaptabilidade",
    "Gerenciamento de tempo",
    "Pensamento crítico",
    "Atenção aos detalhes",
  ],

  // Idiomas
  languages: [
    { language: "Português", proficiency: "Nativo" },
    { language: "Inglês", proficiency: "Intermediário" },
    { language: "Espanhol", proficiency: "Intermediário" },
  ],

  // Certificações destacadas (complemento para os certificados já criados)
  featuredCertifications: [
    "Algoritmos com JavaScript II",
    "Lógica de programação",
    "JavaScript I: Algoritmos de Ordenação",
    "Versionamento de Código com Git e Github",
    "Introdução ao AI-102 com a Microsoft",
    "Elas Lideram",
  ],
};

// Função para renderizar a seção de experiência
function renderExperience() {
  const experienceSection = document.getElementById("experienceSection");
  if (!experienceSection) return;

  // Limpar o conteúdo existente
  experienceSection.innerHTML = "";

  curriculumData.experience.forEach((exp) => {
    const expItem = document.createElement("div");
    expItem.className = "experience-item";

    let responsibilitiesList = "";
    if (exp.responsibilities && exp.responsibilities.length > 0) {
      responsibilitiesList = `
          <ul class="custom-list">
            ${exp.responsibilities.map((resp) => `<li>${resp}</li>`).join("")}
          </ul>
        `;
    }

    let technologiesTags = "";
    if (exp.technologies && exp.technologies.length > 0) {
      technologiesTags = `
          <div class="experience-technologies">
            ${exp.technologies
              .map((tech) => `<span class="tag">${tech}</span>`)
              .join("")}
          </div>
        `;
    }

    expItem.innerHTML = `
        <h3>${exp.position}</h3>
        <div class="experience-date">${exp.period}</div>
        <div class="experience-company">${exp.company}</div>
        ${
          exp.location
            ? `<div class="experience-location"><i class="fas fa-map-marker-alt"></i> ${exp.location}</div>`
            : ""
        }
        <p>${exp.description}</p>
        ${responsibilitiesList}
        ${technologiesTags}
      `;

    experienceSection.appendChild(expItem);
  });
}

// Função para renderizar a seção de educação
function renderEducation() {
  const educationSection = document.getElementById("educationSection");
  if (!educationSection) return;

  // Limpar o conteúdo existente
  educationSection.innerHTML = "";

  curriculumData.education.forEach((edu) => {
    const eduItem = document.createElement("div");
    eduItem.className = "education-item";

    eduItem.innerHTML = `
        <h3>${edu.degree}</h3>
        <div class="education-date">${edu.period}</div>
        <div class="education-institution">${edu.institution}</div>
        <p>${edu.description}</p>
      `;

    educationSection.appendChild(eduItem);
  });
}

// Função para renderizar projetos
function renderProjects() {
  const projectsSection = document.getElementById("projectsSection");
  if (!projectsSection) return;

  // Limpar o conteúdo existente
  projectsSection.innerHTML = "";

  curriculumData.projects.forEach((project) => {
    const projectItem = document.createElement("div");
    projectItem.className = "project-item";

    projectItem.innerHTML = `
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <div class="project-technologies">
          ${project.technologies
            .map((tech) => `<span class="tag">${tech}</span>`)
            .join("")}
        </div>
        ${
          project.link !== "#"
            ? `<a href="${project.link}" class="btn-small" target="_blank"><i class="fab fa-github"></i> Ver Código</a>`
            : ""
        }
      `;

    projectsSection.appendChild(projectItem);
  });
}

// Função para renderizar habilidades técnicas
function renderTechnicalSkills() {
  const skillsGrid = document.getElementById("technicalSkillsGrid");
  if (!skillsGrid) return;

  // Limpar o conteúdo existente
  skillsGrid.innerHTML = "";

  curriculumData.technicalSkills.forEach((skill) => {
    const skillItem = document.createElement("div");
    skillItem.className = "skill-item";
    skillItem.setAttribute("data-level", skill.level.toLowerCase());

    skillItem.innerHTML = `
        ${skill.name}
        <span class="skill-level">${skill.level}</span>
      `;

    skillsGrid.appendChild(skillItem);
  });
}

// Função para renderizar soft skills
function renderSoftSkills() {
  const softSkillsGrid = document.getElementById("softSkillsGrid");
  if (!softSkillsGrid) return;

  // Limpar o conteúdo existente
  softSkillsGrid.innerHTML = "";

  curriculumData.softSkills.forEach((skill) => {
    const skillItem = document.createElement("div");
    skillItem.className = "skill-item";
    skillItem.textContent = skill;

    softSkillsGrid.appendChild(skillItem);
  });
}

// Função para renderizar idiomas
function renderLanguages() {
  const languagesGrid = document.getElementById("languagesGrid");
  if (!languagesGrid) return;

  // Limpar o conteúdo existente
  languagesGrid.innerHTML = "";

  curriculumData.languages.forEach((lang) => {
    const langItem = document.createElement("div");
    langItem.className = "skill-item";
    langItem.innerHTML = `
        ${lang.language}
        <span class="language-level">${lang.proficiency}</span>
      `;

    languagesGrid.appendChild(langItem);
  });
}

// Função para renderizar informações pessoais
function renderPersonalInfo() {
  const elements = {
    personalName: document.getElementById("personalName"),
    personalTitle: document.getElementById("personalTitle"),
    personalAbout: document.getElementById("personalAbout"),
    personalEmail: document.getElementById("personalEmail"),
    personalPhone: document.getElementById("personalPhone"),
    personalLocation: document.getElementById("personalLocation"),
  };

  // Verificar e atualizar cada elemento, se existir
  if (elements.personalName)
    elements.personalName.textContent = curriculumData.personalInfo.name;
  if (elements.personalTitle)
    elements.personalTitle.textContent = curriculumData.personalInfo.title;
  if (elements.personalAbout)
    elements.personalAbout.textContent = curriculumData.personalInfo.about;
  if (elements.personalEmail)
    elements.personalEmail.textContent = curriculumData.personalInfo.email;
  if (elements.personalPhone)
    elements.personalPhone.textContent = curriculumData.personalInfo.phone;
  if (elements.personalLocation)
    elements.personalLocation.textContent =
      curriculumData.personalInfo.location;

  // Links sociais
  const githubLink = document.getElementById("githubLink");
  const linkedinLink = document.getElementById("linkedinLink");

  if (githubLink) githubLink.href = curriculumData.personalInfo.github;
  if (linkedinLink) linkedinLink.href = curriculumData.personalInfo.linkedin;
}

// Função para inicializar todo o currículo
function initCurriculum() {
  renderPersonalInfo();
  renderExperience();
  renderEducation();
  //   renderProjects();
  renderTechnicalSkills();
  renderSoftSkills();
  renderLanguages();
}

// Inicializar quando o documento estiver pronto
document.addEventListener("DOMContentLoaded", initCurriculum);
