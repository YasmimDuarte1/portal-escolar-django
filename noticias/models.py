from django.conf import settings
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Tag(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
    tags = models.ManyToManyField(Tag, related_name='noticias', blank=True)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.titulo


class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username
