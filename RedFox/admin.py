from django.contrib import admin

from RedFox.models import Partida, Compra, Time, Ingresso, ItensCompra


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


admin.site.register(Partida)
admin.site.register(Time)
admin.site.register(Ingresso)



@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]