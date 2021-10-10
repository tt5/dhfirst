from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('hello', include('hello.urls')),
    path('admin/', admin.site.urls),
]
