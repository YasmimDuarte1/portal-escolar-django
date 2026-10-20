# Mão na Massa: Portal Escolar

Projeto Django da prática "Mão na Massa: Portal Escolar": projeto `portal_escolar`, app `noticias` com quatro models e seus relacionamentos (`ForeignKey`, `ManyToManyField` e `OneToOneField`), CRUD completo pelo Django Admin e telas públicas de listagem/detalhes para Categoria, Tag e Notícia.

## Estrutura

- Projeto Django: `portal_escolar/`
- App: `noticias/`
  - `Categoria`: `nome`
  - `Tag`: `titulo`
  - `Noticia`: `titulo`, `texto`, `categoria` (**ForeignKey** para Categoria, 1:N) e `tags` (**ManyToManyField** para Tag, N:M)
  - `Perfil`: `bio`, `usuario` (**OneToOneField** para o model `User` do Django, 1:1)
- Todos os models registrados no Admin (cadastrar, editar e remover)
- Telas públicas:
  - `/` — listagem de notícias
  - `/noticias/<id>/` — detalhe de uma notícia (com links para a categoria e as tags)
  - `/categorias/` — listagem de categorias
  - `/categorias/<id>/` — detalhe de uma categoria (com as notícias associadas)
  - `/tags/` — listagem de tags
  - `/tags/<id>/` — detalhe de uma tag (com as notícias associadas)

## Como rodar

```bash
cd portal_escolar_django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/admin/` para cadastrar categorias, tags, notícias e perfis, e `http://127.0.0.1:8000/` para ver as telas públicas.

## Banco de dados

O `db.sqlite3` já contém dados de exemplo cadastrados pelo Admin (categorias, tags, uma notícia relacionada a elas e um perfil vinculado a um usuário), para demonstrar o fluxo de ponta a ponta.
