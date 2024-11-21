import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Actividad
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..Scripts.arbol import Arbol

@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def newproject(request):
    try:
        user = request.user
        data = json.loads(request.body)
        nombre = data["nombre"]
        url = Arbol(data)
        Json = data
        Actividad.objects.create(nombre=nombre, json=Json, url=url, usuario=user)
        return HttpResponse(status=201) 
    except Exception as e:
        return HttpResponse(status=400)
