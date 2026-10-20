from django.contrib import admin

from .models import Categoria, Noticia, Perfil, Tag


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    list_filter = ('categoria', 'tags')
    search_fields = ('titulo', 'texto')
    filter_horizontal = ('tags',)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio')
    search_fields = ('usuario__username',)
