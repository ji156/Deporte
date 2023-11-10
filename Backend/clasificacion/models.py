from django.db import models


class ClasificacionLaLiga(models.Model):
    # Define los campos del modelo que coincidan con la estructura de la tabla existente en la base de datos
    nombre_equipo = models.CharField(db_column='nombre_equipo')
    posicion = models.IntegerField(db_column='posicion')
    Puntos = models.IntegerField(db_column='puntos')
    PJ = models.IntegerField(db_column='PJ')
    PG = models.IntegerField(db_column='PG')
    PE = models.IntegerField(db_column='PE')
    PP = models.IntegerField(db_column='PP')
    GF = models.IntegerField(db_column='GF')
    GC = models.IntegerField(db_column='GC')

    class Meta:
        # Especifica el nombre de la tabla existente en la base de datos
        db_table = 'clasificacion_laliga'
