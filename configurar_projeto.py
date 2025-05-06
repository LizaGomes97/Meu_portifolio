#!/usr/bin/env python3
"""
Script para automatizar a configuração do projeto Django para o portfólio.
Este script cria a estrutura do projeto, copia os arquivos estáticos e prepara o ambiente.
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

# Cores para mensagens no terminal
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'

def print_verde(texto):
    print(f"{VERDE}{texto}{RESET}")

def print_amarelo(texto):
    print(f"{AMARELO}{texto}{RESET}")

def print_vermelho(texto):
    print(f"{VERMELHO}{texto}{RESET}")

def executar_comando(comando, descricao=None):
    """Executa um comando shell e exibe saída formatada."""
    if descricao:
        print_amarelo(f"\n{descricao}...")
    
    try:
        resultado = subprocess.run(comando, shell=True, check=True, 
                                   stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                   text=True)
        print_verde(f"✓ Comando executado com sucesso: {comando}")
        return True, resultado.stdout
    except subprocess.CalledProcessError as e:
        print_vermelho(f"✗ Erro ao executar: {comando}")
        print_vermelho(f"  Erro: {e.stderr}")
        return False, e.stderr

def verificar_requisitos():
    """Verifica se os requisitos necessários estão instalados."""
    print_amarelo("\nVerificando requisitos...")
    
    # Verificar Python
    versao_python = sys.version_info
    if versao_python.major < 3 or (versao_python.major == 3 and versao_python.minor < 8):
        print_vermelho("✗ Python 3.8 ou superior é necessário.")
        sys.exit(1)
    else:
        print_verde(f"✓ Python {versao_python.major}.{versao_python.minor}.{versao_python.micro} encontrado.")
    
    # Verificar pip
    sucesso, saida = executar_comando("pip --version", "Verificando pip")
    if not sucesso:
        print_vermelho("✗ pip não encontrado. Por favor, instale pip primeiro.")
        sys.exit(1)
    
    # Verificar virtualenv
    sucesso, saida = executar_comando("pip show virtualenv", "Verificando virtualenv")
    if not sucesso:
        print_amarelo("! virtualenv não encontrado. Instalando...")
        executar_comando("pip install virtualenv", "Instalando virtualenv")

def criar_estrutura_projeto():
    """Cria a estrutura básica do projeto Django."""
    pasta_projeto = input("\nDigite o nome da pasta para o seu projeto [portfolio_django]: ").strip() or "portfolio_django"
    
    # Criar diretório do projeto
    print_amarelo(f"\nCriando diretório do projeto: {pasta_projeto}")
    if os.path.exists(pasta_projeto):
        sobrescrever = input(f"A pasta {pasta_projeto} já existe. Sobrescrever? (s/N): ").lower() == 's'
        if sobrescrever:
            shutil.rmtree(pasta_projeto)
        else:
            print_amarelo("Usando a pasta existente...")
    
    if not os.path.exists(pasta_projeto):
        os.makedirs(pasta_projeto)
    
    # Mudar para o diretório do projeto
    os.chdir(pasta_projeto)
    print_verde(f"✓ Diretório de trabalho: {os.getcwd()}")
    
    # Criar e ativar ambiente virtual
    executar_comando("virtualenv venv", "Criando ambiente virtual")
    
    # Instalar dependências
    print_amarelo("\nInstalando dependências...")
    if sys.platform == "win32":
        pip_path = os.path.join("venv", "Scripts", "pip")
    else:
        pip_path = os.path.join("venv", "bin", "pip")
    
    executar_comando(f"{pip_path} install django pillow requests", "Instalando Django e pacotes necessários")
    
    # Criar projeto Django
    print_amarelo("\nCriando projeto Django...")
    if sys.platform == "win32":
        django_admin = os.path.join("venv", "Scripts", "django-admin")
    else:
        django_admin = os.path.join("venv", "bin", "django-admin")
    
    executar_comando(f"{django_admin} startproject portfolio_projeto .", "Criando projeto Django")
    
    # Criar aplicativo portfolio
    print_amarelo("\nCriando aplicativo portfolio...")
    if sys.platform == "win32":
        manage_py = "python manage.py"
    else:
        manage_py = "./manage.py"
    
    executar_comando(f"{manage_py} startapp portfolio", "Criando aplicativo portfolio")
    
    # Criar diretórios para templates e arquivos estáticos
    print_amarelo("\nCriando estrutura de diretórios...")
    diretorios = [
        os.path.join("portfolio", "templates"),
        os.path.join("portfolio", "static", "css"),
        os.path.join("portfolio", "static", "js"),
        os.path.join("portfolio", "static", "img"),
        os.path.join("media", "projetos"),
    ]
    
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)
        print_verde(f"✓ Diretório criado: {diretorio}")
    
    return pasta_projeto

def baixar_arquivos_template():
    """Baixa os arquivos de template do GitHub ou outro repositório."""
    # Aqui você poderia implementar a lógica para baixar templates ou copiar de um repositório
    
    print_amarelo("\nPara completar a configuração, você precisa:")
    print_amarelo("1. Copiar seus arquivos estáticos para a pasta portfolio/static/")
    print_amarelo("2. Criar os arquivos de modelo conforme documentação")
    print_amarelo("3. Configurar o settings.py conforme documentação")
    
    # Instruções para o próximo passo
    print_verde("\n✓ Estrutura do projeto criada com sucesso!")
    print_amarelo("\nPara continuar, siga os seguintes passos:")
    
    if sys.platform == "win32":
        print_amarelo("1. Ative o ambiente virtual: .\\venv\\Scripts\\activate")
    else:
        print_amarelo("1. Ative o ambiente virtual: source venv/bin/activate")
    
    print_amarelo("2. Execute as migrações: python manage.py makemigrations")
    print_amarelo("3. Aplique as migrações: python manage.py migrate")
    print_amarelo("4. Crie um superusuário: python manage.py createsuperuser")
    print_amarelo("5. Importe seus dados: python manage.py shell < importar_dados.py")
    print_amarelo("6. Inicie o servidor: python manage.py runserver")
    print_amarelo("\nAcesse o site em: http://127.0.0.1:8000/")
    print_amarelo("Acesse o admin em: http://127.0.0.1:8000/admin/")

def main():
    """Função principal do script."""
    print_verde("\n" + "="*50)
    print_verde("   CONFIGURAÇÃO DO PROJETO DJANGO - PORTFÓLIO   ")
    print_verde("="*50 + "\n")
    
    verificar_requisitos()
    pasta_projeto = criar_estrutura_projeto()
    baixar_arquivos_template()

if __name__ == "__main__":
    main()