from django.contrib import admin

from .models import Usuario, Editora, Livro, Emprestimo

admin.site.register(Usuario)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Emprestimo)