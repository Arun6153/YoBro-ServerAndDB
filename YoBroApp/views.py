from django.http import HttpResponse, HttpResponseBadRequest
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def userSignUp(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf'))
        newUser = User(
            email=data['email'], password=data['password'], address=data['address'])
        newUser.save()
        return HttpResponse(status=201)
    else:
        return HttpResponseBadRequest('<h3>Not Allowed</h3>')

@csrf_exempt
def userLogin(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest('<h3>Not Allowed</h3>')