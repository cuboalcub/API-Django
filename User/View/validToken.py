import json
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def validToken(request):
    try:
        # Obtener el encabezado Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Token '):
            return JsonResponse({'error': 'Token no proporcionado'}, status=400)

        # Extraer el token
        token_key = auth_header.split(' ')[1].strip()
        
        # Verificar si el token existe
        token = Token.objects.get(key=token_key)
        return JsonResponse({'success': True, 'token': token.key}, status=200)

    except Token.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Token no válido'}, status=400)

    except Exception as e:
        return JsonResponse({'success': False, 'error': f'Error interno: {str(e)}'}, status=500)
