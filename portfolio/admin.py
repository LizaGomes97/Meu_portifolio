from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Projeto, TagProjeto, Certificado, TagCertificado,
    Experiencia, ResponsabilidadeExperiencia, TecnologiaExperiencia,
    Educacao, HabilidadeTecnica, SoftSkill, Idioma,
    InformacaoPessoal, Interesse
)

# Customização do site admin
admin.site.site_header = 'Administração do Portfólio'
admin.site.site_title = 'Painel Administrativo'
admin.site.index_title = 'Bem-vinda ao Painel de Gerenciamento do Portfólio'


# Inlines para modelos relacionados
class TagProjetoInline(admin.TabularInline):
    model = TagProjeto
    extra = 1
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


class TagCertificadoInline(admin.TabularInline):
    model = TagCertificado
    extra = 1
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


class ResponsabilidadeExperienciaInline(admin.TabularInline):
    model = ResponsabilidadeExperiencia
    extra = 1
    verbose_name = "Responsabilidade"
    verbose_name_plural = "Responsabilidades"


class TecnologiaExperienciaInline(admin.TabularInline):
    model = TecnologiaExperiencia
    extra = 1
    verbose_name = "Tecnologia"
    verbose_name_plural = "Tecnologias"


class InteresseInline(admin.TabularInline):
    model = Interesse
    extra = 1
    verbose_name = "Interesse"
    verbose_name_plural = "Interesses"


# Admin para Projeto
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'exibir_imagem', 'descricao_curta', 'data_criacao', 'exibir_tags')
    list_filter = ('data_criacao', 'tags__nome')
    search_fields = ('titulo', 'descricao', 'descricao_curta')
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ('exibir_imagem_grande', 'data_criacao', 'exibir_demo')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'slug', 'descricao_curta', 'descricao')
        }),
        ('Mídia', {
            'fields': ('imagem', 'exibir_imagem_grande')
        }),
        ('Links', {
            'fields': ('repo_url', 'demo_url', 'exibir_demo')
        }),
    )
    inlines = [TagProjetoInline]
    save_on_top = True

    def exibir_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.imagem.url)
        return "Sem imagem"
    exibir_imagem.short_description = 'Imagem'

    def exibir_imagem_grande(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="300" style="max-height: 300px; object-fit: contain; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />', obj.imagem.url)
        return "Sem imagem"
    exibir_imagem_grande.short_description = 'Pré-visualização'
    
    def exibir_demo(self, obj):
        if obj.demo_url:
            return format_html(
                '<div style="max-width:600px; border-radius:8px; overflow:hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">'
                '<iframe src="{}" width="100%" height="300" style="border:none; display:block;"></iframe>'
                '</div>',
                obj.demo_url
            )
        return "Sem demonstração disponível"
    exibir_demo.short_description = 'Pré-visualização da Demo'

    def exibir_tags(self, obj):
        tags = obj.tags.all()
        if tags:
            return ', '.join([t.nome for t in tags])
        return "Sem tags"
    exibir_tags.short_description = 'Tags'


# Admin para Certificado
@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'emissor', 'data', 'exibir_logo', 'exibir_tags')
    list_filter = ('emissor', 'tags__nome')
    search_fields = ('titulo', 'emissor', 'descricao')
    fieldsets = (
        ('Informações do Certificado', {
            'fields': ('titulo', 'emissor', 'data', 'descricao')
        }),
        ('Mídia e Links', {
            'fields': ('logo', 'exibir_logo_grande', 'url_credencial', 'id_credencial')
        }),
    )
    readonly_fields = ('exibir_logo_grande',)
    inlines = [TagCertificadoInline]
    save_on_top = True

    def exibir_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: contain; border-radius: 5px;" />', obj.logo)
        return "Sem logo"
    exibir_logo.short_description = 'Logo'

    def exibir_logo_grande(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="200" style="max-height: 200px; object-fit: contain; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />', obj.logo)
        return "Sem logo"
    exibir_logo_grande.short_description = 'Pré-visualização do Logo'

    def exibir_tags(self, obj):
        tags = obj.tags.all()
        if tags:
            return ', '.join([t.nome for t in tags])
        return "Sem tags"
    exibir_tags.short_description = 'Tags'


# Admin para Experiência
@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'periodo', 'localizacao', 'ordem')
    list_filter = ('empresa',)
    search_fields = ('cargo', 'empresa', 'descricao')
    list_editable = ('ordem',)
    fieldsets = (
        ('Informações do Cargo', {
            'fields': ('cargo', 'empresa', 'periodo')
        }),
        ('Detalhes', {
            'fields': ('localizacao', 'descricao', 'ordem')
        }),
    )
    inlines = [ResponsabilidadeExperienciaInline, TecnologiaExperienciaInline]
    save_on_top = True


# Admin para Educação
@admin.register(Educacao)
class EducacaoAdmin(admin.ModelAdmin):
    list_display = ('grau', 'instituicao', 'periodo')
    search_fields = ('grau', 'instituicao', 'descricao')
    fieldsets = (
        ('Informações do Curso', {
            'fields': ('grau', 'instituicao', 'periodo', 'descricao')
        }),
    )


# Admin para Habilidade Técnica
@admin.register(HabilidadeTecnica)
class HabilidadeTecnicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'exibir_nivel_barra')
    list_filter = ('nivel',)
    search_fields = ('nome',)
    list_editable = ('nivel',)

    def exibir_nivel_barra(self, obj):
        niveis = {
            'Básico': 33,
            'Intermediário': 66,
            'Avançado': 100
        }
        nivel_valor = niveis.get(obj.nivel, 0)
        cor = '#0ff'  # Cor ciano do tema
        if obj.nivel == 'Avançado':
            cor = '#f0f'  # Cor magenta para avançado
        
        return format_html(
            '<div style="width:100px; background-color:#333; height:10px; border-radius:5px;">'
            '<div style="width:{}%; background-color:{}; height:10px; border-radius:5px;"></div>'
            '</div>', 
            nivel_valor, cor
        )
    exibir_nivel_barra.short_description = 'Nível'


# Admin para SoftSkill
@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# Admin para Idioma
@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'proficiencia', 'exibir_proficiencia_barra')
    list_filter = ('proficiencia',)
    search_fields = ('nome', 'proficiencia')
    list_editable = ('proficiencia',)

    def exibir_proficiencia_barra(self, obj):
        niveis = {
            'Básico': 33,
            'Intermediário': 66,
            'Avançado': 90,
            'Nativo': 100
        }
        nivel_valor = niveis.get(obj.proficiencia, 0)
        cor = '#ff0'  # Cor amarela
        
        return format_html(
            '<div style="width:100px; background-color:#333; height:10px; border-radius:5px;">'
            '<div style="width:{}%; background-color:{}; height:10px; border-radius:5px;"></div>'
            '</div>', 
            nivel_valor, cor
        )
    exibir_proficiencia_barra.short_description = 'Nível'


# Admin para Informações Pessoais
@admin.register(InformacaoPessoal)
class InformacaoPessoalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo', 'email', 'telefone')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'titulo', 'sobre')
        }),
        ('Contato', {
            'fields': ('email', 'telefone', 'localizacao')
        }),
        ('Redes Sociais', {
            'fields': ('linkedin', 'github')
        }),
        ('Outras Informações', {
            'fields': ('disponibilidade',)
        }),
    )
    inlines = [InteresseInline]

    def has_add_permission(self, request):
        # Limitar a uma única instância de informação pessoal
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)