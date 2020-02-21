from django.urls import path
from YoBroApp import views


urlpatterns = [
    path('register/', views.userSignUp),
    path('login/', views.userLogin),
]
