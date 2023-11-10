from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    avatar = models.ImageField(
        upload_to='avatar/', default='avatar/default.png')
    # esto es para saber si esta activo o no
    status = models.BooleanField(default=False)
    # esto es para saber cuando se creo
    created_at = models.DateTimeField(auto_now_add=True)
    # esto es para saber cuando se actualizo
    updated_at = models.DateTimeField(auto_now=True)
    # esto es para saber cuando se elimino
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + ' ' + self.email + ' ' + str(self.status)

    class Meta:
        db_table = 'login'
        verbose_name = 'Login'
