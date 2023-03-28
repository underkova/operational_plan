from . import views
from django.urls import path

urlpatterns = [
    # path('',views.index),
    path('', views.instructor)]  #адская скобочка

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
]