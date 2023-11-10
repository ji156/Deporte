from django.db import models


class CalendarioLaLiga(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')
    jornada = models.CharField(db_column='jornada')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_laliga'


class CalendarioLaLigaFemenina(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_laliga_femenina'


class CalendarioPremierLeague(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_premierleague'


class CalendarioSerieA(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_seriea'


class CalendarioBundesliga(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_bundesliga'


class CalendarioLigue1(models.Model):
    # Campos que coinciden con la base de datos
    local = models.CharField(db_column='local')
    visitante = models.CharField(db_column='visitante')
    resultado = models.CharField(db_column='resultado')

    class Meta:
        # nombre de la tabla en la base de datos
        db_table = 'calendario_ligue1'
