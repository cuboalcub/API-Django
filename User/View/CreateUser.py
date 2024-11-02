import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data["username"]
            password = data["password"]
            email = data["email"]
            user = User.objects.create_user(username=username, password=password, email=email)
            return HttpResponse(status=201)
        except Exception as e:
            return HttpResponse(status=400)
