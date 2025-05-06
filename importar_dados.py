"""
Script para importar dados do seu portfólio atual para o Django.
Este script deve ser executado no shell do Django usando:
python manage.py shell < importar_dados.py
"""
import os
import django
import json
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.text import slugify
from pathlib import Path

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portifolio_projeto.settings')
django.setup()

# Importar modelos
from portfolio.models import (
    Projeto, TagProjeto, Certificado, TagCertificado,
    Experiencia, ResponsabilidadeExperiencia, TecnologiaExperiencia,
    Educacao, HabilidadeTecnica, SoftSkill, Idioma,
    InformacaoPessoal, Interesse
)

# Diretório base do projeto antigo (ajuste conforme necessário)
BASE_DIR = Path(__file__).resolve().parent

def carregar_json_de_js(caminho_arquivo, nome_variavel):
    """Extrai dados JSON de um arquivo JavaScript."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            
            # Encontrar a declaração da variável
            inicio = conteudo.find(f"{nome_variavel} = ")
            if inicio == -1:
                inicio = conteudo.find(f"const {nome_variavel} = ")
                if inicio == -1:
                    raise ValueError(f"Variável {nome_variavel} não encontrada no arquivo")
                inicio += len(f"const {nome_variavel} = ")
            else:
                inicio += len(f"{nome_variavel} = ")
            
            # Encontrar o fim da declaração (pode ser terminada com ; ou não)
            # Vamos procurar o último ]
            fim = conteudo.rfind(";")
            if fim == -1 or conteudo.rfind("]") > fim:
                fim = len(conteudo)
            else:
                conteudo = conteudo[:fim]
                fim = conteudo.rfind("]") + 1
                
            dados_json = conteudo[inicio:fim]
            
            # Limpar comentários, se houver
            linhas = dados_json.split('\n')
            linhas_limpas = []
            for linha in linhas:
                if '//' in linha:
                    linha = linha[:linha.index('//')]
                linhas_limpas.append(linha)
            dados_json = '\n'.join(linhas_limpas)
            
            return json.loads(dados_json)
    except Exception as e:
        print(f"Erro ao carregar dados de {caminho_arquivo}: {e}")
        return []

def importar_projetos():
    """Importa os projetos do arquivo JS para o Django."""
    print("\n=== Importando Projetos ===")
    
    # Limpar dados existentes
    Projeto.objects.all().delete()
    TagProjeto.objects.all().delete()
    
    # Carregar dados do arquivo JS
    caminho_js = os.path.join(BASE_DIR, 'js', 'main.js')
    projetos_dados = carregar_json_de_js(caminho_js, 'projects')
    
    contador = 0
    for projeto_dado in projetos_dados:
        # Criar o projeto
        projeto = Projeto(
            titulo=projeto_dado['title'],
            slug=slugify(projeto_dado['id']),
            descricao=projeto_dado['description'],
            descricao_curta=projeto_dado['shortDescription'],
            repo_url=projeto_dado['repoUrl'],
            demo_url=projeto_dado.get('demoUrl'),
            iframe_url=projeto_dado.get('iframeUrl')
        )
        
        # Salvar para gerar o slug
        projeto.save()
        
        # Adicionar imagem (isso irá fazer download da imagem e salvar localmente)
        # Nota: isso funciona apenas para URLs acessíveis
        imagem_caminho = projeto_dado.get('image', '')
        if imagem_caminho:
            if imagem_caminho.startswith('http'):
                try:
                    response = requests.get(imagem_caminho)
                    if response.status_code == 200:
                        img_temp = NamedTemporaryFile(delete=True)
                        img_temp.write(response.content)
                        img_temp.flush()
                        
                        nome_arquivo = os.path.basename(imagem_caminho)
                        projeto.imagem.save(nome_arquivo, File(img_temp), save=True)
                except Exception as e:
                    print(f"Erro ao baixar imagem para {projeto.titulo}: {e}")
            else:
                # Tenta carregar de um caminho local
                try:
                    caminho_completo = os.path.join(BASE_DIR, imagem_caminho)
                    if os.path.exists(caminho_completo):
                        with open(caminho_completo, 'rb') as f:
                            nome_arquivo = os.path.basename(imagem_caminho)
                            projeto.imagem.save(nome_arquivo, File(f), save=True)
                except Exception as e:
                    print(f"Erro ao carregar imagem local para {projeto.titulo}: {e}")
        
        # Adicionar tags
        for tag_nome in projeto_dado.get('tags', []):
            TagProjeto.objects.create(projeto=projeto, nome=tag_nome)
        
        contador += 1
        print(f"Projeto importado: {projeto.titulo}")
    
    print(f"Total de projetos importados: {contador}")

def importar_certificados():
    """Importa os certificados do arquivo JS para o Django."""
    print("\n=== Importando Certificados ===")
    
    # Limpar dados existentes
    Certificado.objects.all().delete()
    TagCertificado.objects.all().delete()
    
    # Carregar dados do arquivo JS
    caminho_js = os.path.join(BASE_DIR, 'js', 'certificates.js')
    certificados_dados = carregar_json_de_js(caminho_js, 'certificates')
    
    contador = 0
    for cert_dado in certificados_dados:
        # Criar o certificado
        certificado = Certificado(
            titulo=cert_dado['title'],
            emissor=cert_dado['issuer'],
            data=cert_dado['date'],
            descricao=cert_dado['description'],
            logo=cert_dado['logo'],
            url_credencial=cert_dado.get('credentialUrl'),
            id_credencial=cert_dado.get('credentialId')
        )
        
        # Salvar o certificado
        certificado.save()
        
        # Adicionar tags
        for tag_nome in cert_dado.get('tags', []):
            TagCertificado.objects.create(certificado=certificado, nome=tag_nome)
        
        contador += 1
        print(f"Certificado importado: {certificado.titulo}")
    
    print(f"Total de certificados importados: {contador}")

def importar_curriculo():
    """Importa os dados do currículo do arquivo JS para o Django."""
    print("\n=== Importando Dados do Currículo ===")
    
    # Limpar dados existentes
    InformacaoPessoal.objects.all().delete()
    Interesse.objects.all().delete()
    Experiencia.objects.all().delete()
    ResponsabilidadeExperiencia.objects.all().delete()
    TecnologiaExperiencia.objects.all().delete()
    Educacao.objects.all().delete()
    HabilidadeTecnica.objects.all().delete()
    SoftSkill.objects.all().delete()
    Idioma.objects.all().delete()
    
    # Carregar dados do arquivo JS
    caminho_js = os.path.join(BASE_DIR, 'js', 'curriculum.js')
    dados_curriculo = carregar_json_de_js(caminho_js, 'curriculumData')
    
    # Adicionar informações pessoais
    info_pessoal_dados = dados_curriculo.get('personalInfo', {})
    if info_pessoal_dados:
        info_pessoal = InformacaoPessoal(
            nome=info_pessoal_dados.get('name', ''),
            titulo=info_pessoal_dados.get('title', ''),
            email=info_pessoal_dados.get('email', ''),
            telefone=info_pessoal_dados.get('phone', ''),
            localizacao=info_pessoal_dados.get('location', ''),
            linkedin=info_pessoal_dados.get('linkedin', ''),
            github=info_pessoal_dados.get('github', ''),
            sobre=info_pessoal_dados.get('about', ''),
            disponibilidade=info_pessoal_dados.get('availability', '')
        )
        info_pessoal.save()
        
        # Adicionar interesses
        for nome_interesse in info_pessoal_dados.get('interests', []):
            Interesse.objects.create(info_pessoal=info_pessoal, nome=nome_interesse)
        
        print("Informações pessoais importadas")

    # Adicionar experiências
    contador_exp = 0
    for i, exp_dado in enumerate(dados_curriculo.get('experience', [])):
        experiencia = Experiencia(
            cargo=exp_dado.get('position', ''),
            empresa=exp_dado.get('company', ''),
            periodo=exp_dado.get('period', ''),
            localizacao=exp_dado.get('location', ''),
            descricao=exp_dado.get('description', ''),
            ordem=i
        )
        experiencia.save()
        
        # Adicionar responsabilidades
        for resp_texto in exp_dado.get('responsibilities', []):
            ResponsabilidadeExperiencia.objects.create(
                experiencia=experiencia,
                descricao=resp_texto
            )
        
        # Adicionar tecnologias
        for tech_nome in exp_dado.get('technologies', []):
            TecnologiaExperiencia.objects.create(
                experiencia=experiencia,
                nome=tech_nome
            )
        
        contador_exp += 1
        print(f"Experiência importada: {experiencia.cargo} - {experiencia.empresa}")
    
    print(f"Total de experiências importadas: {contador_exp}")

    # Adicionar educação
    contador_edu = 0
    for edu_dado in dados_curriculo.get('education', []):
        educacao = Educacao(
            grau=edu_dado.get('degree', ''),
            instituicao=edu_dado.get('institution', ''),
            periodo=edu_dado.get('period', ''),
            descricao=edu_dado.get('description', '')
        )
        educacao.save()
        contador_edu += 1
        print(f"Educação importada: {educacao.grau}")
    
    print(f"Total de itens de educação importados: {contador_edu}")

    # Adicionar habilidades técnicas
    contador_tech = 0
    for skill_dado in dados_curriculo.get('technicalSkills', []):
        habilidade = HabilidadeTecnica(
            nome=skill_dado.get('name', ''),
            nivel=skill_dado.get('level', 'Básico')
        )
        habilidade.save()
        contador_tech += 1
        print(f"Habilidade técnica importada: {habilidade.nome}")
    
    print(f"Total de habilidades técnicas importadas: {contador_tech}")

    # Adicionar soft skills
    contador_soft = 0
    for skill_nome in dados_curriculo.get('softSkills', []):
        SoftSkill.objects.create(nome=skill_nome)
        contador_soft += 1
        print(f"Soft skill importada: {skill_nome}")
    
    print(f"Total de soft skills importadas: {contador_soft}")

    # Adicionar idiomas
    contador_idiomas = 0
    for idioma_dado in dados_curriculo.get('languages', []):
        idioma = Idioma(
            nome=idioma_dado.get('language', ''),
            proficiencia=idioma_dado.get('proficiency', '')
        )
        idioma.save()
        contador_idiomas += 1
        print(f"Idioma importado: {idioma.nome}")
    
    print(f"Total de idiomas importados: {contador_idiomas}")

def executar_importacao():
    """Executa todas as importações."""
    print("Iniciando importação de dados para o Django...")
    importar_projetos()
    importar_certificados()
    importar_curriculo()
    print("\nImportação concluída com sucesso!")

if __name__ == "__main__":
    executar_importacao()