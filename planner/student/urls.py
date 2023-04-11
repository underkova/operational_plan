from django.urls import path
from student.views import *


#urlpatterns = [
   # path('',views.index),
 #   path('', views.student)
#]
urlpatterns = [
    path('', ops, name='student'),
    path('test/', test, name='student'),
]