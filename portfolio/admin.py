from django.contrib import admin
from .models import (
    Projeto, TagProjeto, Certificado, TagCertificado,
    Experiencia, ResponsabilidadeExperiencia, TecnologiaExperiencia,
    Educacao, HabilidadeTecnica, SoftSkill, Idioma,
    InformacaoPessoal, Interesse
)

class TagProjetoInline(admin.TabularInline):
    model = TagProjeto
    extra = 1

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao_curta', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [TagProjetoInline]

class TagCertificadoInline(admin.TabularInline):
    model = TagCertificado
    extra = 1

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'emissor', 'data')
    search_fields = ('titulo', 'emissor', 'descricao')
    inlines = [TagCertificadoInline]

class ResponsabilidadeExperienciaInline(admin.TabularInline):
    model = ResponsabilidadeExperiencia
    extra = 1

class TecnologiaExperienciaInline(admin.TabularInline):
    model = TecnologiaExperiencia
    extra = 1

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'periodo')
    search_fields = ('cargo', 'empresa', 'descricao')
    list_editable = ('periodo',)
    inlines = [ResponsabilidadeExperienciaInline, TecnologiaExperienciaInline]

@admin.register(Educacao)
class EducacaoAdmin(admin.ModelAdmin):
    list_display = ('grau', 'instituicao', 'periodo')
    search_fields = ('grau', 'instituicao', 'descricao')

@admin.register(HabilidadeTecnica)
class HabilidadeTecnicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    list_filter = ('nivel',)
    search_fields = ('nome',)

@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'proficiencia')
    search_fields = ('nome', 'proficiencia')

class InteresseInline(admin.TabularInline):
    model = Interesse
    extra = 1

@admin.register(InformacaoPessoal)
class InformacaoPessoalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo', 'email')
    inlines = [InteresseInline]