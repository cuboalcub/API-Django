import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]
        user = User.objects.get(username=username)

        # Verifica la contraseña
        if user.check_password(password):
            # Genera el token de acceso y refresco
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Retorna el token en la respuesta
            return JsonResponse({
                'access': access_token,
                'refresh': refresh_token
            }, status=200)
        else:
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=401)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Error en la solicitud'}, status=400)
