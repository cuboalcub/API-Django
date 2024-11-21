from django.db import models
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from ..models import Actividad

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id','nombre', 'tiempo_optimista', 'tiempo_medio', 'tiempo_pesimista']

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def obtener_actividades(request):
    usuario = request.user  
    print(usuario.username)
    actividades = Actividad.objects.filter(usuario=usuario)
    serializer = ActividadSerializer(actividades, many=True)
    return Response(serializer.data)
