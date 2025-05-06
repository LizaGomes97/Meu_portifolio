"""
Script para importar especificamente os dados do currículo para o Django.
Execute este script com:
python manage.py shell < importar_curriculo.py
"""
import os
import django
import json
from django.conf import settings

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portifolio_projeto.settings')
django.setup()

# Importar modelos
from portfolio.models import (
    InformacaoPessoal, Interesse, Experiencia, ResponsabilidadeExperiencia, 
    TecnologiaExperiencia, Educacao, HabilidadeTecnica, SoftSkill, Idioma
)

def importar_curriculo():
    """Importa os dados do currículo a partir do arquivo JSON."""
    print("\n=== Importando Dados do Currículo ===")
    
    # Limpar dados existentes
    print("Limpando dados existentes...")
    InformacaoPessoal.objects.all().delete()
    Interesse.objects.all().delete()
    Experiencia.objects.all().delete()
    ResponsabilidadeExperiencia.objects.all().delete()
    TecnologiaExperiencia.objects.all().delete()
    Educacao.objects.all().delete()
    HabilidadeTecnica.objects.all().delete()
    SoftSkill.objects.all().delete()
    Idioma.objects.all().delete()
    
    # Caminho para o arquivo JSON
    json_path = os.path.join(settings.BASE_DIR, 'js', 'curriculum.json')
    
    try:
        # Carregar os dados do arquivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            dados_curriculo = json.load(file)
        
        # Verificar se os dados foram carregados corretamente
        if not dados_curriculo:
            print("Erro: Nenhum dado encontrado no arquivo JSON.")
            return
            
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
            print(f"Informação pessoal importada: {info_pessoal.nome}")
            
            # Adicionar interesses
            for nome_interesse in info_pessoal_dados.get('interests', []):
                interesse = Interesse(info_pessoal=info_pessoal, nome=nome_interesse)
                interesse.save()
                print(f"Interesse importado: {nome_interesse}")
        
        # Adicionar experiências
        contador_experiencias = 0
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
            contador_experiencias += 1
            print(f"Experiência importada: {experiencia.cargo} - {experiencia.empresa}")
            
            # Adicionar responsabilidades
            for resp_texto in exp_dado.get('responsibilities', []):
                resp = ResponsabilidadeExperiencia(experiencia=experiencia, descricao=resp_texto)
                resp.save()
                print(f"  Responsabilidade: {resp_texto[:30]}...")
            
            # Adicionar tecnologias
            for tech_nome in exp_dado.get('technologies', []):
                tech = TecnologiaExperiencia(experiencia=experiencia, nome=tech_nome)
                tech.save()
                print(f"  Tecnologia: {tech_nome}")
        
        print(f"Total de experiências importadas: {contador_experiencias}")
        
        # Adicionar educação
        contador_educacao = 0
        for edu_dado in dados_curriculo.get('education', []):
            educacao = Educacao(
                grau=edu_dado.get('degree', ''),
                instituicao=edu_dado.get('institution', ''),
                periodo=edu_dado.get('period', ''),
                descricao=edu_dado.get('description', '')
            )
            educacao.save()
            contador_educacao += 1
            print(f"Educação importada: {educacao.grau}")
        
        print(f"Total de itens de educação importados: {contador_educacao}")
        
        # Adicionar habilidades técnicas
        contador_tech_skills = 0
        for skill_dado in dados_curriculo.get('technicalSkills', []):
            habilidade = HabilidadeTecnica(
                nome=skill_dado.get('name', ''),
                nivel=skill_dado.get('level', 'Básico')
            )
            habilidade.save()
            contador_tech_skills += 1
            print(f"Habilidade técnica importada: {habilidade.nome} - {habilidade.nivel}")
        
        print(f"Total de habilidades técnicas importadas: {contador_tech_skills}")
        
        # Adicionar soft skills
        contador_soft_skills = 0
        for skill_nome in dados_curriculo.get('softSkills', []):
            skill = SoftSkill(nome=skill_nome)
            skill.save()
            contador_soft_skills += 1
            print(f"Soft skill importada: {skill_nome}")
        
        print(f"Total de soft skills importadas: {contador_soft_skills}")
        
        # Adicionar idiomas
        contador_idiomas = 0
        for idioma_dado in dados_curriculo.get('languages', []):
            idioma = Idioma(
                nome=idioma_dado.get('language', ''),
                proficiencia=idioma_dado.get('proficiency', '')
            )
            idioma.save()
            contador_idiomas += 1
            print(f"Idioma importado: {idioma.nome} - {idioma.proficiencia}")
        
        print(f"Total de idiomas importados: {contador_idiomas}")
        
        print("Importação do currículo concluída com sucesso!")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {json_path}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
    except Exception as e:
        print(f"Erro durante a importação: {e}")

# Executar a importação
importar_curriculo()

if __name__ == "__main__":
    importar_curriculo()