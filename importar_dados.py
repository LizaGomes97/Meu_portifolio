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
                    inicio = conteudo.find(f"var {nome_variavel} = ")
                    if inicio == -1:
                        raise ValueError(f"Variável {nome_variavel} não encontrada no arquivo")
                    inicio += len(f"var {nome_variavel} = ")
                else:
                    inicio += len(f"const {nome_variavel} = ")
            else:
                inicio += len(f"{nome_variavel} = ")
            
            # Encontrar o fim da declaração
            profundidade = 0
            em_string = False
            escape = False
            fim = inicio
            
            # Para arrays
            if conteudo[inicio].strip() == '[':
                for i in range(inicio, len(conteudo)):
                    char = conteudo[i]
                    
                    if not em_string:
                        if char == '[':
                            profundidade += 1
                        elif char == ']':
                            profundidade -= 1
                            if profundidade == 0:
                                fim = i + 1
                                break
                    
                    if char == '"' and not escape:
                        em_string = not em_string
                    
                    escape = char == '\\' and not escape
            
            # Para objetos
            elif conteudo[inicio].strip() == '{':
                for i in range(inicio, len(conteudo)):
                    char = conteudo[i]
                    
                    if not em_string:
                        if char == '{':
                            profundidade += 1
                        elif char == '}':
                            profundidade -= 1
                            if profundidade == 0:
                                fim = i + 1
                                break
                    
                    if char == '"' and not escape:
                        em_string = not em_string
                    
                    escape = char == '\\' and not escape
            
            if fim <= inicio:
                raise ValueError("Não foi possível encontrar o fim da declaração")
            
            # Extrair o JSON
            js_data = conteudo[inicio:fim]
            
            # Converter formato JavaScript para JSON válido
            # Substituir nomes de propriedades sem aspas
            import re
            # Regex para encontrar nomes de propriedades sem aspas
            js_data = re.sub(r'([{,])\s*([a-zA-Z0-9_$]+)\s*:', r'\1"\2":', js_data)
            
            # Substituir aspas simples por aspas duplas
            js_data = js_data.replace("'", '"')
            
            # Remover vírgulas finais em arrays e objetos
            js_data = re.sub(r',\s*([}\]])', r'\1', js_data)
            
            try:
                import json
                return json.loads(js_data)
            except json.JSONDecodeError as e:
                print(f"Erro ao analisar JSON: {e}")
                print(f"JSON inválido: {js_data[:100]}...")
                return {}
            
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
    caminho_json = os.path.join(BASE_DIR, 'js', 'certificates.json')
    certificados_dados = carregar_json_direto(caminho_json)
    
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
    caminho_json = os.path.join(BASE_DIR, 'js', 'curriculum.json')
    dados_curriculo = carregar_json_direto(caminho_json)
    # Verificar se dados_curriculo é uma lista ou um dicionário
    if not dados_curriculo:
        print("Nenhum dado de currículo encontrado.")
        return
        
    if isinstance(dados_curriculo, list):
        print("Os dados do currículo estão em formato de lista, convertendo para dicionário...")
        # Se for uma lista com um único elemento que é um dicionário, use-o
        if len(dados_curriculo) == 1 and isinstance(dados_curriculo[0], dict):
            dados_curriculo = dados_curriculo[0]
        else:
            print("Formato de dados inesperado. Criando estrutura padrão.")
            dados_curriculo = {
                'personalInfo': {},
                'experience': [],
                'education': [],
                'technicalSkills': [],
                'softSkills': [],
                'languages': []
            }

def carregar_json_direto(caminho_arquivo):
    """Carrega dados diretamente de um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            import json
            return json.load(arquivo)
    except Exception as e:
        print(f"Erro ao carregar JSON de {caminho_arquivo}: {e}")
        return []

def executar_importacao():
    """Executa todas as importações."""
    print("Iniciando importação de dados para o Django...")
    importar_projetos()
    importar_certificados()
    importar_curriculo()
    print("\nImportação concluída com sucesso!")

if __name__ == "__main__":
    executar_importacao()