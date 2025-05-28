from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def logout(request):
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Token '):
            return JsonResponse({'error': 'Token no proporcionado'}, status=400)

        token_key = auth_header.split(' ')[1]
        token = Token.objects.get(key=token_key)
        token.delete()  # Invalida el token
        return JsonResponse({'message': 'Sesión cerrada correctamente'}, status=200)

    except Token.DoesNotExist:
        return JsonResponse({'error': 'Token no válido'}, status=400)
