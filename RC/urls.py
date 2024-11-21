from django.urls import path
from .View import newproject
from .View import viewprojects
from .View import viewall
urlpatterns = [
    path('add', newproject.Actividad),
     path('view', viewprojects.obtener_actividades)
]


