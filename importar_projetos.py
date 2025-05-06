import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_projeto.settings')
django.setup()

from portfolio.models import Projeto, TagProjeto
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests
import json

# Dados dos projetos do seu arquivo JS atual
projetos_dados = [
    # Cole aqui o array 'projects' do seu arquivo main.js
]

for projeto_dado in projetos_dados:
    # Criar o projeto
    projeto = Projeto(
        titulo=projeto_dado['title'],
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
    if 'image' in projeto_dado and projeto_dado['image'].startswith('http'):
        try:
            response = requests.get(projeto_dado['image'])
            if response.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()
                
                nome_arquivo = os.path.basename(projeto_dado['image'])
                projeto.imagem.save(nome_arquivo, File(img_temp), save=True)
        except Exception as e:
            print(f"Erro ao baixar imagem para {projeto.titulo}: {e}")
    
    # Adicionar tags
    for tag_nome in projeto_dado.get('tags', []):
        TagProjeto.objects.create(projeto=projeto, nome=tag_nome)
    
    print(f"Projeto importado: {projeto.titulo}")