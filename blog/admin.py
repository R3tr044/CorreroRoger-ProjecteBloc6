from django.contrib import admin
from .models import Post, Author, Tag # Importa tus modelos

# Registra los modelos para que aparezcan en el panel
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)