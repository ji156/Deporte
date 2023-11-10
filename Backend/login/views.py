# views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test


@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def guardar_registro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Validar y guardar en la base de datos
        if password == confirm_password:
            hashed_password = make_password(password)
            login = Login(email=email, password=hashed_password)
            login.save()
            return JsonResponse({'message': 'Registro exitoso'})
        else:
            return JsonResponse({'error': 'Las contraseñas no coinciden'})

    return JsonResponse({'error': 'Este endpoint solo acepta solicitudes POST'})
