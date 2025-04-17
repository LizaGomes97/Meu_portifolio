// Dados dos certificados
const certificates = [
  {
    id: "cert1",
    title: "Versionamento de Código com Git e Github",
    issuer: "DIO",
    date: "Outubro 2024",
    description: "Aprendendo a versionar e publicar codigo",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Git", "GitHub"],
    credentialUrl: "#",
    // credentialId: "RGSBCZ30",
  },
  {
    id: "cert2",
    title: "JavaScript I: Algoritmos De Ordenação",
    issuer: "Alura",
    date: "Março 2024",
    description:
      "Durante as aulas, aprendi sobre a importância dos algoritmos e como eles estão presentes no nosso dia a dia. Além disso, consegui extrair a lógica dos algoritmos e traduzi-la em código, explorando diferentes formas de resolver o mesmo problema. Agora, também entendo como utilizar algoritmos em conjunto e os conceitos básicos para a análise de complexidade",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEZkMsv5FwbDA/company-logo_200_200/company-logo_200_200/0/1710187635900/aluracursos_logo?e=1750291200&v=beta&t=M1lWXsi8_ut6Ye9wRC5iWHp6ORZ8U4cH5AaDCh5ZRnQ",
    tags: ["JavaScript", "Algoritmos", "Back-end"],
    credentialUrl:
      "https://cursos.alura.com.br/certificate/162ca1e4-1ab9-48e5-bae9-a19472208a43?lang",
    // credentialId: "162ca1e4-1ab9-48e5-bae9-a19472208a43",
  },
  {
    id: "cert3",
    title: "Algoritmos com JavaScript II",
    issuer: "Alura",
    date: "Abril 2025",
    description:
      "Aprofundamento em algoritmos avançados com JavaScript, incluindo quickSort e técnicas de otimização.",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEZkMsv5FwbDA/company-logo_200_200/company-logo_200_200/0/1710187635900/aluracursos_logo?e=1750291200&v=beta&t=M1lWXsi8_ut6Ye9wRC5iWHp6ORZ8U4cH5AaDCh5ZRnQ",
    tags: ["Algoritmos", "Análise de algoritmo", "JavaScript"],
    credentialUrl: "#",
    // credentialId: "dfdd795b-ef37-49d1-97e6-3349291e815b",
  },
  {
    id: "cert4",
    title: "Lógica de programação",
    issuer: "Alura",
    date: "Abril 2025",
    description:
      "Fundamentos da lógica de programação aplicados em JavaScript com projetos práticos.",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEZkMsv5FwbDA/company-logo_200_200/company-logo_200_200/0/1710187635900/aluracursos_logo?e=1750291200&v=beta&t=M1lWXsi8_ut6Ye9wRC5iWHp6ORZ8U4cH5AaDCh5ZRnQ",
    tags: ["JavaScript", "Algoritmos", "Análise de algoritmo"],
    credentialUrl: "#",
    // credentialId: "b018ad9b-9c36-4af8-8ba6-9ab6b0bc7d37",
  },
  {
    id: "cert5",
    title: "Lógica de programação (Avançado)",
    issuer: "Alura",
    date: "Abril 2025",
    description:
      "Aprofundamento em técnicas de lógica de programação com foco em JavaScript e GitHub.",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEZkMsv5FwbDA/company-logo_200_200/company-logo_200_200/0/1710187635900/aluracursos_logo?e=1750291200&v=beta&t=M1lWXsi8_ut6Ye9wRC5iWHp6ORZ8U4cH5AaDCh5ZRnQ",
    tags: ["JavaScript", "GitHub", "Lógica de Programação"],
    credentialUrl: "#",
    // credentialId: "6ddb3677-c97a-4b7c-bde4-ee53ee23e286",
  },
  {
    id: "cert6",
    title: "Imersão Front-End 2ª Edição",
    issuer: "Alura",
    date: "Fevereiro 2025",
    description:
      "Desenvolvimento de projeto front-end completo utilizando HTML, CSS, JavaScript e React.js.",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEZkMsv5FwbDA/company-logo_200_200/company-logo_200_200/0/1710187635900/aluracursos_logo?e=1750291200&v=beta&t=M1lWXsi8_ut6Ye9wRC5iWHp6ORZ8U4cH5AaDCh5ZRnQ",
    tags: ["React.js", "JavaScript", "HTML", "CSS", "Front-end"],
    credentialUrl: "#",
    // credentialId: "",
  },
  {
    id: "cert7",
    title: "Entendendo Comunicação Client x Server",
    issuer: "DIO",
    date: "Outubro 2024",
    description:
      "Compreensão da arquitetura e comunicação entre cliente e servidor na web.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Web", "Client-Server", "Redes"],
    credentialUrl: "#",
    // credentialId: "UIY65XRZ",
  },
  {
    id: "cert8",
    title: "Boas-vindas a Formação Rumo à Certificação AWS Cloud Practitioner",
    issuer: "DIO",
    date: "2024",
    description:
      "Introdução aos conceitos fundamentais da AWS para preparação da certificação Cloud Practitioner.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["AWS CloudFormation", "Cloud", "AWS"],
    credentialUrl: "#",
    // credentialId: "AHUN0QSX",
  },
  {
    id: "cert9",
    title: "Conceitos Fundamentais de IA",
    issuer: "DIO",
    date: "2024",
    description:
      "Introdução aos fundamentos de Inteligência Artificial e principais conceitos.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["IA", "Machine Learning", "Inteligência Artificial"],
    credentialUrl: "#",
    // credentialId: "WSQ38ONR",
  },
  {
    id: "cert10",
    title: "Conceitos de Visão Computacional",
    issuer: "DIO",
    date: "2024",
    description:
      "Fundamentos de visão computacional e suas aplicações na Inteligência Artificial.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Visão Computacional", "IA", "Processamento de Imagens"],
    credentialUrl: "#",
    // credentialId: "HFRH3UXE",
  },
  {
    id: "cert11",
    title: "Contribuindo em um Projeto Open Source no GitHub",
    issuer: "DIO",
    date: "2024",
    description:
      "Aprendi a contribuir em projetos de código aberto usando GitHub e boas práticas de colaboração.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Git", "Git BASH", "GitHub", "Open Source"],
    credentialUrl: "#",
    // credentialId: "D4XAA1SK",
  },
  {
    id: "cert12",
    title: "Desafio de Projetos: Crie um Portfólio Vencedor",
    issuer: "DIO",
    date: "2024",
    description:
      "Desenvolvimento de portfólio profissional para destacar projetos e habilidades.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Portfólio", "Front-end", "Carreira"],
    credentialUrl: "#",
    // credentialId: "DAMOSZZP",
  },
  {
    id: "cert13",
    title:
      "Desafio de código: Aperfeiçoe sua lógica e pensamento computacional",
    issuer: "DIO",
    date: "2024",
    description:
      "Resolução de desafios de programação para melhorar lógica e pensamento algorítmico.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Lógica de Programação", "Algoritmos", "Desafios de Código"],
    credentialUrl: "#",
    // credentialId: "QB19UCLS",
  },
  {
    id: "cert14",
    title: "Elas Lideram",
    issuer: "RD Saúde",
    date: "2024",
    description:
      "Programa focado em liderança feminina e desenvolvimento de habilidades de gestão.",
    logo: "https://media.licdn.com/dms/image/v2/D4D0BAQEDHD-82rSbgA/company-logo_200_200/company-logo_200_200/0/1720039549617/rdsaudeoficial_logo?e=1750291200&v=beta&t=h7TiIHf2ahIqgklHkSqKbSUM8AwrPBqQj8-EJOn0xpM",
    tags: ["Liderança", "Soft Skills", "Mulheres na Tecnologia"],
    credentialUrl: "#",
    // credentialId: "",
  },
  {
    id: "cert15",
    title: "Entendendo HTML semântico",
    issuer: "DIO",
    date: "2024",
    description:
      "Uso correto de tags HTML semânticas para melhorar a acessibilidade e SEO de websites.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["HTML", "HTML Semântico", "Front-end"],
    credentialUrl: "#",
    // credentialId: "ZJBRWI00",
  },
  {
    id: "cert16",
    title: "Estruturando HTML + formatação",
    issuer: "DIO",
    date: "2024",
    description:
      "Estruturação e formatação de documentos HTML para desenvolvimento web moderno.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["HTML", "CSS", "Front-end"],
    credentialUrl: "#",
    // credentialId: "X0EZZ2TP",
  },
  {
    id: "cert17",
    title: "Fundamentos de aprendizado de máquinas",
    issuer: "DIO",
    date: "2024",
    description:
      "Conceitos fundamentais de Machine Learning e suas aplicações práticas.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Machine Learning", "IA", "Data Science"],
    credentialUrl: "#",
    // credentialId: "LZ275EK8",
  },
  {
    id: "cert18",
    title: "Introdução a AI-102 com a Microsoft",
    issuer: "Microsoft",
    date: "2024",
    description:
      "Introdução à certificação AI-102: Designing and Implementing an Azure AI Solution.",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/2048px-Microsoft_logo.svg.png",
    tags: ["Azure", "IA", "Microsoft"],
    credentialUrl: "#",
    // credentialId: "KU4M9GW0",
  },
  {
    id: "cert19",
    title: "Introdução ao AI-900",
    issuer: "DIO",
    date: "2024",
    description:
      "Fundamentos para a certificação Microsoft Azure AI Fundamentals (AI-900).",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Azure", "IA", "Microsoft"],
    credentialUrl: "#",
    // credentialId: "DGQRV6RX",
  },
  {
    id: "cert20",
    title: "Introdução ao Desenvolvimento Front-end",
    issuer: "DIO",
    date: "2024",
    description:
      "Fundamentos de desenvolvimento front-end utilizando HTML, CSS e JavaScript.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["HTML", "JavaScript", "CSS", "Front-end"],
    credentialUrl: "#",
    // credentialId: "",
  },
  {
    id: "cert21",
    title: "Introdução ao HTML na prática",
    issuer: "DIO",
    date: "2024",
    description:
      "Aplicação prática de HTML, incluindo desenvolvimento de formulários e estruturas básicas.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["HTML", "HTML5", "Formulários"],
    credentialUrl: "#",
    // credentialId: "DWXWETBE",
  },
  {
    id: "cert22",
    title: "Power BI",
    issuer: "Microsoft",
    date: "2024",
    description:
      "Análise de dados e criação de dashboards e relatórios utilizando Microsoft Power BI.",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/2048px-Microsoft_logo.svg.png",
    tags: ["Power BI", "Business Intelligence", "Análise de Dados"],
    credentialUrl: "#",
    // credentialId: "",
  },
  {
    id: "cert23",
    title: "Primeiros passos com AWS",
    issuer: "DIO",
    date: "2024",
    description:
      "Introdução aos serviços e conceitos fundamentais da Amazon Web Services.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["AWS Lambda", "AWS IAM", "AWS", "Cloud"],
    credentialUrl: "#",
    // credentialId: "JTPNBH9R",
  },
  {
    id: "cert24",
    title: "Trabalhando com Machine Learning na Prática no Azure ML",
    issuer: "DIO",
    date: "2024",
    description:
      "Implementação prática de modelos de Machine Learning utilizando Azure Machine Learning.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["Azure", "Machine Learning", "IA", "Cloud"],
    credentialUrl: "#",
    // credentialId: "BFYZVQBC",
  },
  {
    id: "cert25",
    title: "Trabalhando com formulários em HTML",
    issuer: "DIO",
    date: "2024",
    description:
      "Desenvolvimento e estilização de formulários HTML para aplicações web.",
    logo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKw5JRBqrwiDIDd3ZUlG-Q6vqVLBTdOh6w-A&s",
    tags: ["HTML", "Formulários", "Front-end"],
    credentialUrl: "#",
    // credentialId: "HWB3AE0G",
  },
];

// Função para renderizar a página de certificados
function renderCertificates() {
  const certificatesGrid = document.getElementById("certificatesGrid");

  // Limpar o conteúdo existente
  certificatesGrid.innerHTML = "";

  // Adicionar cada certificado ao grid
  certificates.forEach((certificate) => {
    const certificateCard = document.createElement("div");
    certificateCard.className = "certificate-card";

    // Criar o HTML para o certificado
    certificateCard.innerHTML = `
        <div class="certificate-content">
          <div class="certificate-logo">
            <img src="${certificate.logo}" alt="Logo de ${certificate.issuer}">
          </div>
          <div class="certificate-info">
            <h3>${certificate.title}</h3>
            <div class="certificate-issuer">${certificate.issuer}</div>
            <div class="certificate-date">${certificate.date}</div>
            <p>${certificate.description}</p>
            <div class="certificate-tags">
              ${certificate.tags
                .map((tag) => `<span class="tag">${tag}</span>`)
                .join("")}
            </div>
          </div>
        </div>
        <div class="certificate-footer">
          <a href="${
            certificate.credentialUrl
          }" class="btn-small">Ver Credencial</a>
          ${
            certificate.credentialId
              ? `<div class="certificate-id">ID: ${certificate.credentialId}</div>`
              : ""
          }
        </div>
      `;

    // Adicionar o certificado ao grid
    certificatesGrid.appendChild(certificateCard);
  });
}

// Inicializar quando o documento estiver pronto
document.addEventListener("DOMContentLoaded", renderCertificates);
