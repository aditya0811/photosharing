# todos/urls.py
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.ListMeme.as_view())),
    path('<int:pk>/', csrf_exempt(views.DetailMeme.as_view())),
    path('<int:pk>', csrf_exempt(views.DetailMeme.as_view())),
]