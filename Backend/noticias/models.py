from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


def validate_image_size(value):
    filesize = value.size
    if filesize > 250 * 1024:  # 250 KB (in bytes)
        raise ValidationError('La imagen no puede ser mayor de 250 KB.')


class Noticias(models.Model):
    tags = models.CharField(max_length=25, default='')
    titulo = models.CharField(max_length=100)
    noticia = models.TextField(default='')
    imagen = models.ImageField(upload_to='noticias', validators=[
                               validate_image_size], null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    leidas = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo + ' - ' + self.noticia + ' - ' + str(self.fecha)

    class Meta:
        db_table = 'noticias'
        ordering = ['-fecha']
        verbose_name_plural = 'Noticias'
