from django.contrib import admin
from .models import *

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Projeto)
admin.site.register(Grupo)
admin.site.register(AlunoProjeto)
