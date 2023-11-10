from django.contrib import admin
from .models import EscudosLaLiga
from .models import EscudosPremier
from .models import EscudosSeriea
from .models import EscudosBundesliga
from .models import EscudosLigue1

# Register your models here.
admin.site.register(EscudosLaLiga)
admin.site.register(EscudosPremier)
admin.site.register(EscudosSeriea)
admin.site.register(EscudosBundesliga)
admin.site.register(EscudosLigue1)
