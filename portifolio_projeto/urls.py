from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from portfolio.admin_dashboard import portfolio_admin_site
from portfolio.models import (
    Projeto, TagProjeto, Certificado, TagCertificado,
    Experiencia, ResponsabilidadeExperiencia, TecnologiaExperiencia,
    Educacao, HabilidadeTecnica, SoftSkill, Idioma,
    InformacaoPessoal, Interesse
)

# Importar classes Admin personalizadas
from portfolio.admin import (
    ProjetoAdmin, CertificadoAdmin, ExperienciaAdmin, EducacaoAdmin,
    HabilidadeTecnicaAdmin, SoftSkillAdmin, IdiomaAdmin, InformacaoPessoalAdmin
)

# Registrar modelos no admin personalizado
portfolio_admin_site.register(Projeto, ProjetoAdmin)
portfolio_admin_site.register(Certificado, CertificadoAdmin)
portfolio_admin_site.register(Experiencia, ExperienciaAdmin)
portfolio_admin_site.register(Educacao, EducacaoAdmin)
portfolio_admin_site.register(HabilidadeTecnica, HabilidadeTecnicaAdmin)
portfolio_admin_site.register(SoftSkill, SoftSkillAdmin)
portfolio_admin_site.register(Idioma, IdiomaAdmin)
portfolio_admin_site.register(InformacaoPessoal, InformacaoPessoalAdmin)

# Também podemos registrar os modelos do Django Auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
portfolio_admin_site.register(User, UserAdmin)
portfolio_admin_site.register(Group, GroupAdmin)

urlpatterns = [
    # Substituir o admin padrão pelo nosso admin personalizado
    path('admin/', portfolio_admin_site.urls),
    path('', include('portfolio.urls')),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)