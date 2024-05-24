from django.urls import path
from . import views

urlpatterns = [
    path('', views.fibonacci_number, name='fib'),
]