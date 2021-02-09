# todos/urls.py
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
	path('<int:id>/',csrf_exempt(views.search)),
	path('',csrf_exempt(views.index)),
	path('ed/<int:id>',csrf_exempt(views.ed)),
]