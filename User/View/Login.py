import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.models import Token


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            return JsonResponse({'error': 'Usuario y contraseña son requeridos'}, status=400)

        user = User.objects.get(username=username)
        if user.check_password(password):
            token = Token.objects.create(user=user)
            return JsonResponse({'token': token.key}, status=200)
        else:
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=401)
    
    except User.DoesNotExist:
        print("Usuario no encontrado")
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
    except json.JSONDecodeError:
        print("Solicitud JSON no válida")
        return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)
    

    except Exception as e:
        # Incluir mensaje de error para más detalles en el diagnóstico
        print("Error en la solicitud")
        return JsonResponse({'error': f'Error en la solicitud: {str(e)}'}, status=400)
