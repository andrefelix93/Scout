from django.contrib import admin

# Register your models here.
# scouts/admin.py

from django.contrib import admin
from .models import Acao, Partida

admin.site.register(Acao)
admin.site.register(Partida)