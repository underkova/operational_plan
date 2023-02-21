from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.index),
    path('about', views.about),
    path('admin/', admin.site.urls),

]


