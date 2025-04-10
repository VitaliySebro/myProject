from django.contrib import admin
from django.urls import path
from . import views  # якщо view знаходиться в тому ж myproject

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # додай цей рядок для головної
]
