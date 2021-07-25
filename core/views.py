from django.views.generic import TemplateView
from .py.utileria import URL_ENLACE_JSON
import urllib, json
from django.contrib import messages
import gzip
from datetime import datetime
from vuelos.models import Vuelo
from django.db.models import Count

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, *args, **kwargs):
        contexto = super(IndexTemplateView,self).get_context_data(*args, **kwargs)

        try: #Prueba de programación
            datos_json = json.loads( #Se obtiene el archivo json de la URL y se descomprimen los bytes para cargarlo en un diccionario
                gzip.decompress(
                    urllib.request.urlopen(URL_ENLACE_JSON).read()
                ).decode("utf-8"),
            )

            programacion = {}
            programacion["respuestas_contestadas"] = 0
            programacion["respuestas_no_contestadas"] = 0

            for diccionario in datos_json["items"]: #Se iteran las respuestas, cada una es un diccionario
                if diccionario["is_answered"]: #Se obtiene la cantidad de respuestas contestadas y las no contestadas
                    programacion["respuestas_contestadas"] += 1
                else:
                    programacion["respuestas_no_contestadas"] += 1
                
                if "respuesta_menor_vistas" in programacion: #Se obtiene el titulo de la respuesta con menor cantidad de vistas
                    if diccionario["view_count"] <= programacion["respuesta_menor_vistas"]["vistas"]:
                        programacion["respuesta_menor_vistas"]["titulo_respuesta"] = diccionario["title"]
                        programacion["respuesta_menor_vistas"]["vistas"] = diccionario["view_count"]
                else:
                    programacion["respuesta_menor_vistas"] = {"titulo_respuesta":diccionario["title"], "vistas":diccionario["view_count"]}
                
                if "fecha_creacion" in programacion: #Se obtiene el titulo de la respuesta más antigua y el de la más actual
                    fecha_creacion = datetime.fromtimestamp(diccionario["creation_date"]) #El formato de la fecha en el json está en timestamp por lo que hay que modificarlo
                    if fecha_creacion <= programacion["fecha_creacion"]["respuesta_antigua"]["fecha"]:
                        programacion["fecha_creacion"]["respuesta_antigua"]["titulo_respuesta"] = diccionario["title"]
                        programacion["fecha_creacion"]["respuesta_antigua"]["fecha"] = fecha_creacion
                    
                    if fecha_creacion >= programacion["fecha_creacion"]["respuesta_actual"]["fecha"]:
                        programacion["fecha_creacion"]["respuesta_actual"]["titulo_respuesta"] = diccionario["title"]
                        programacion["fecha_creacion"]["respuesta_actual"]["fecha"] = fecha_creacion
                else:
                    fecha_creacion = datetime.fromtimestamp(diccionario["creation_date"])
                    programacion["fecha_creacion"] = {
                        "respuesta_antigua":{"titulo_respuesta":diccionario["title"], "fecha":fecha_creacion},
                        "respuesta_actual":{"titulo_respuesta":diccionario["title"], "fecha":fecha_creacion}
                    }
        except urllib.error.URLError: #Se lanza esta excepción en caso que no se pueda acceder a la URL del json, por lo que se omite la prueba de Programación
            messages.info(self.request, f"No se ha podido acceder a la URL {URL_ENLACE_JSON}; por lo que se omitira la prueba de \"Programación\", por favor intente más tarde.")
        except Exception as error:
            messages.error(self.request, f"Ha ocurrido un error en la prueba de programación: {error}")
        else:
            contexto["programacion"] = programacion
            print(f"""
                \rPregunta 6 Se imprimen las respuestas anteriores
                    \r  Pregunta 2
                        \r      Número de respuestas contestadas: {contexto["programacion"]["respuestas_contestadas"]}
                        \r      Número de respuestas no contestadas: {contexto["programacion"]["respuestas_no_contestadas"]}
                    \r  Pregunta 3
                        \r      Pendiente
                    \r  Pregunta 4
                        \r      Respuesta con menor número de vistas: {contexto["programacion"]["respuesta_menor_vistas"]["titulo_respuesta"]}
                        \r      Cantidad de vistas: {contexto["programacion"]["respuesta_menor_vistas"]["vistas"]}
                    \r  Pregunta 5
                        \r      Respuesta más antigua: {programacion["fecha_creacion"]["respuesta_antigua"]["titulo_respuesta"]}
                        \r      Fecha de la respuesta: {programacion["fecha_creacion"]["respuesta_antigua"]["fecha"]}

                        \r      Respuesta más actual: {programacion["fecha_creacion"]["respuesta_actual"]["titulo_respuesta"]}
                        \r      Fecha de la respuesta: {programacion["fecha_creacion"]["respuesta_actual"]["fecha"]}
            """)
        
        try: #Prueba de SQL
            sql = {}
            sql["aeropuerto_mas_vuelos"] = Vuelo.objects.values("aeropuerto__nombre_aeropuerto").annotate(vuelos_por_año = Count("dia__year")).order_by("-vuelos_por_año").first() #Se obtiene el aeropuerto con más vuelos durante el año
            sql["aerolinea_mas_vuelos"] = Vuelo.objects.values("aerolinea__nombre_aerolinea").annotate(vuelos_por_año = Count("dia__year")).order_by("-vuelos_por_año").first() #Se obtiene la aerolínea con más vuelos durante el año
            sql["dia_mas_vuelos"] = Vuelo.objects.values("dia").annotate(vuelos_por_dia = Count("dia")).order_by("-vuelos_por_dia").first() #Se obtiene el día con mayor número de vuelos
            sql["aerolineas_mas_de_2_vuelos_por_dia"] = Vuelo.objects.values("aerolinea__nombre_aerolinea","aerolinea__logo_aerolinea","dia").annotate(vuelos_por_dia = Count("dia")).filter(vuelos_por_dia__gte=2).order_by("-dia", "-vuelos_por_dia") #Se obtiene las aerolíneas que tienen más de 2 vuelos por día
        except Exception as error:
            messages.error(self.request, f"Ha ocurrido un error en la prueba de SQL: {error}")
        else:
            contexto["sql"] = sql

        return contexto