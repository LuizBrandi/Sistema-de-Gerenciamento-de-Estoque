from django.contrib import admin
from .models import Mercadoria, Entrada
from django.contrib.auth.models import Group

admin.site.site_header =  'MStarSupply'

class MercadoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'fabricante',)
    list_filter = ['tipo']
    
# Register your models here.
admin.site.register(Mercadoria, MercadoriaAdmin)
admin.site.register(Entrada)
admin.site.unregister(Group)
