import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["GET"])
def hellouser(request):
    return HttpResponse(json.dumps({'Mensaje': 'hello world'}), status=200)