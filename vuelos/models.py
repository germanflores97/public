from django.db import models

# Create your models here.
class Aerolinea(models.Model):
    nombre_aerolinea = models.CharField(verbose_name="Nombre de la aerolínea", max_length=30)
    logo_aerolinea = models.ImageField(verbose_name="Logo de la aerolínea", upload_to="logos_aerolineas",blank=True, null=True)

    def __str__(self,*args,**kwargs):
        return f"Aerolínea {self.nombre_aerolinea}"

    class Meta:
        db_table = "aerolineas"
        verbose_name = "aerolínea"
        verbose_name_plural = "aerolíneas"

class Aeropuerto(models.Model):
    nombre_aeropuerto = models.CharField(verbose_name="Nombre del aeropuerto", max_length=30)

    def __str__(self,*args,**kwargs):
        return f"Aeropuerto {self.nombre_aeropuerto}"

    class Meta:
        db_table = "aeropuertos"
        verbose_name = "aeropuerto"
        verbose_name_plural = "aeropuertos"

class Movimiento(models.Model):
    descripcion = models.CharField(verbose_name="Descripción del movimiento", max_length=40)

    def __str__(self,*args,**kwargs):
        return f"{self.descripcion}"

    class Meta:
        db_table = "movimientos"
        verbose_name = "movimiento"
        verbose_name_plural = "movimientos"

class Vuelo(models.Model):
    aerolinea = models.ForeignKey(Aerolinea, verbose_name="Aerolínea", on_delete=models.PROTECT)
    aeropuerto = models.ForeignKey(Aeropuerto, verbose_name="Aeropuerto", on_delete=models.PROTECT)
    movimiento = models.ForeignKey(Movimiento, verbose_name="Movimiento", on_delete=models.PROTECT)
    dia = models.DateField(verbose_name="Fecha del vuelo")

    def __str__(self,*args,**kwargs):
        return f"Vuelo del día {self.dia}"
    
    @property
    def campos_ids(self):
        return f"{self.aerolinea_id}, {self.aeropuerto_id}, {self.movimiento_id}"
    
    class Meta:
        db_table = "vuelos"
        verbose_name = "vuelo"
        verbose_name_plural = "vuelos"