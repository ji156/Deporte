# Generated by Django 4.2.7 on 2023-11-08 18:01

from django.db import migrations, models
import noticias.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='noticias', validators=[noticias.models.validate_image_size])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
