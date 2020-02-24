from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def userSignUp(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf'))
        newUser = User(
            email=data['email'], password=data['password'], address=data['address'], name=data['name'])
        newUser.save()
        return HttpResponse(status=201)
    return HttpResponseBadRequest('<h3>Not Allowed</h3>')


@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf'))
        email = data['email']
        password = data['password']
        if email and password:
            UserTableData = User.objects.all()
            val = UserTableData.filter(email=email, password=password).values()
            if val:
                return HttpResponse(JsonResponse({"data":list(val)}),status=200)
    return HttpResponseBadRequest('<h3>Not Allowed</h3>')

@csrf_exempt
def home(request, id):
    if request.method == 'GET':
        UserTableData = User.objects.all()
        val = UserTableData.exclude(id=id).values()

        # print(val.object)
        return JsonResponse({"data":list(val)})
    return HttpResponseBadRequest('<h3>Not Allowed</h3>')

