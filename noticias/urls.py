from django.urls import path

from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.noticia_lista, name='noticia_lista'),
    path('noticias/<int:noticia_id>/', views.noticia_detalhe, name='noticia_detalhe'),
    path('categorias/', views.categoria_lista, name='categoria_lista'),
    path('categorias/<int:categoria_id>/', views.categoria_detalhe, name='categoria_detalhe'),
    path('tags/', views.tag_lista, name='tag_lista'),
    path('tags/<int:tag_id>/', views.tag_detalhe, name='tag_detalhe'),
]
