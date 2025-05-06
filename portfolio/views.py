from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import (
    Projeto, Certificado, Experiencia, Educacao, 
    HabilidadeTecnica, SoftSkill, Idioma, InformacaoPessoal
)


class IndexView(ListView):
    model = Projeto
    template_name = 'index.html'
    context_object_name = 'projetos'

    def get_queryset(self):
        return Projeto.objects.all()


class ProjetoDetalheView(DetailView):
    model = Projeto
    template_name = 'projeto_detalhe.html'
    context_object_name = 'projeto'
    slug_url_kwarg = 'slug'


class CertificadosView(ListView):
    model = Certificado
    template_name = 'certificados.html'
    context_object_name = 'certificados'

    def get_queryset(self):
        return Certificado.objects.all()


class CurriculoView(TemplateView):
    template_name = 'curriculo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['info_pessoal'] = InformacaoPessoal.objects.first()
        except InformacaoPessoal.DoesNotExist:
            context['info_pessoal'] = None
            
        context['experiencias'] = Experiencia.objects.all()
        context['educacao'] = Educacao.objects.all()
        context['habilidades_tecnicas'] = HabilidadeTecnica.objects.all()
        context['soft_skills'] = SoftSkill.objects.all()
        context['idiomas'] = Idioma.objects.all()
        
        return context