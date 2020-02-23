from django.urls import include, path
from YoBroApp import views

urlpatterns = [
    path('register/', views.userSignUp),
    path('login/', views.userLogin),
]