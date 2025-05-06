from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descricao = models.TextField()
    descricao_curta = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='projetos/')
    repo_url = models.URLField(verbose_name="URL do Repositório")
    demo_url = models.URLField(verbose_name="URL da Demonstração", blank=True, null=True)
    iframe_url = models.URLField(verbose_name="URL do iframe", blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('projeto_detalhe', kwargs={'slug': self.slug})


class TagProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, related_name='tags', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Tag de Projeto"
        verbose_name_plural = "Tags de Projetos"
    
    def __str__(self):
        return self.nome


class Certificado(models.Model):
    titulo = models.CharField(max_length=200)
    emissor = models.CharField(max_length=100)
    data = models.CharField(max_length=50)  # Mantendo como string para permitir formatos como "Março 2024"
    descricao = models.TextField()
    logo = models.URLField(verbose_name="URL do Logo")
    url_credencial = models.URLField(verbose_name="URL da Credencial", blank=True, null=True)
    id_credencial = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"
        ordering = ['-data']
    
    def __str__(self):
        return f"{self.titulo} - {self.emissor}"


class TagCertificado(models.Model):
    certificado = models.ForeignKey(Certificado, related_name='tags', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Tag de Certificado"
        verbose_name_plural = "Tags de Certificados"
    
    def __str__(self):
        return self.nome


class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    ordem = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
        ordering = ['ordem']
    
    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class ResponsabilidadeExperiencia(models.Model):
    experiencia = models.ForeignKey(Experiencia, related_name='responsabilidades', on_delete=models.CASCADE)
    descricao = models.TextField()
    
    class Meta:
        verbose_name = "Responsabilidade"
        verbose_name_plural = "Responsabilidades"
    
    def __str__(self):
        return self.descricao[:50]


class TecnologiaExperiencia(models.Model):
    experiencia = models.ForeignKey(Experiencia, related_name='tecnologias', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
    
    def __str__(self):
        return self.nome


class Educacao(models.Model):
    grau = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    class Meta:
        verbose_name = "Educação"
        verbose_name_plural = "Educação"
    
    def __str__(self):
        return f"{self.grau} - {self.instituicao}"


class HabilidadeTecnica(models.Model):
    NIVEIS = (
        ('básico', 'Básico'),
        ('intermediário', 'Intermediário'),
        ('avançado', 'Avançado'),
    )
    
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    
    class Meta:
        verbose_name = "Habilidade Técnica"
        verbose_name_plural = "Habilidades Técnicas"
    
    def __str__(self):
        return f"{self.nome} - {self.nivel}"


class SoftSkill(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Soft Skill"
        verbose_name_plural = "Soft Skills"
    
    def __str__(self):
        return self.nome


class Idioma(models.Model):
    nome = models.CharField(max_length=50)
    proficiencia = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"
    
    def __str__(self):
        return f"{self.nome} - {self.proficiencia}"


class InformacaoPessoal(models.Model):
    nome = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    localizacao = models.CharField(max_length=100)
    linkedin = models.URLField(verbose_name="LinkedIn URL")
    github = models.URLField(verbose_name="GitHub URL")
    sobre = models.TextField()
    disponibilidade = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Informação Pessoal"
        verbose_name_plural = "Informações Pessoais"
    
    def __str__(self):
        return self.nome


class Interesse(models.Model):
    info_pessoal = models.ForeignKey(InformacaoPessoal, related_name='interesses', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"
    
    def __str__(self):
        return self.nome