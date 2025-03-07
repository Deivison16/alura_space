from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class ListaFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'descricao', 'foto', 'categoria', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'publicada')
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Fotografia, ListaFotografia)