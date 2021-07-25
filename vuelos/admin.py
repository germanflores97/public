from django.contrib import admin
from .models import Aerolinea,Aeropuerto,Movimiento,Vuelo

# Register your models here.
class AerolineaAdmin(admin.ModelAdmin):
    list_display = ["nombre_aerolinea","logo_aerolinea"]
    search_fields = ["nombre_aerolinea"]
    list_per_page = 25
    ordering = ["id"]
    fieldsets=[
        [
            "Información de la aerolínea",
            {"fields":["id", "nombre_aerolinea","logo_aerolinea"]}
        ]
    ]
    readonly_fields=["id"]

class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ["nombre_aeropuerto"]
    search_fields = ["nombre_aeropuerto"]
    list_per_page = 25
    ordering = ["id"]
    fieldsets=[
        [
            "Información del aeropuerto",
            {"fields":["id", "nombre_aeropuerto"]}
        ]
    ]
    readonly_fields=["id"]

class MovimientoAdmin(admin.ModelAdmin):
    list_display = ["descripcion"]
    search_fields = ["descripcion"]
    list_per_page = 25
    ordering = ["id"]
    fieldsets=[
        [
            "Información del movimiento",
            {"fields":["id", "descripcion"]}
        ]
    ]
    readonly_fields=["id"]

class VueloAdmin(admin.ModelAdmin):
    date_hierarchy = "dia"
    list_display = ["dia", "aerolinea", "aeropuerto", "movimiento","campos_ids"]
    list_filter = ["aerolinea", "aeropuerto", "movimiento"]
    autocomplete_fields = ["aerolinea", "aeropuerto"]
    list_per_page = 25
    ordering = ["-dia"]
    fieldsets=[
        [
            "Fecha del vuelo",
            {"fields":["dia"]}
        ],
        [
            "Información del vuelo",
            {"fields":["aerolinea", "aeropuerto", "movimiento","campos_ids"]}
        ]
    ]
    readonly_fields=["campos_ids"]


#Registramos los módelos en el administrador
admin.site.register(Aerolinea, AerolineaAdmin)
admin.site.register(Aeropuerto, AeropuertoAdmin)
admin.site.register(Movimiento,MovimientoAdmin)
admin.site.register(Vuelo, VueloAdmin)