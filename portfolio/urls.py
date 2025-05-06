from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projeto/<slug:slug>/', views.ProjetoDetalheView.as_view(), name='projeto_detalhe'),
    path('certificados/', views.CertificadosView.as_view(), name='certificados'),
    path('curriculo/', views.CurriculoView.as_view(), name='curriculo'),
]