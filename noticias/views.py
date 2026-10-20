from django.shortcuts import get_object_or_404, render

from .models import Categoria, Noticia, Tag


def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'noticias/categoria_lista.html', {'categorias': categorias})


def categoria_detalhe(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, 'noticias/categoria_detalhe.html', {'categoria': categoria})


def tag_lista(request):
    tags = Tag.objects.all()
    return render(request, 'noticias/tag_lista.html', {'tags': tags})


def tag_detalhe(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    return render(request, 'noticias/tag_detalhe.html', {'tag': tag})


def noticia_lista(request):
    noticias = Noticia.objects.select_related('categoria').all()
    return render(request, 'noticias/noticia_lista.html', {'noticias': noticias})


def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticias/noticia_detalhe.html', {'noticia': noticia})
