from django.urls import path
from . import views

#urlpatterns = [
   # path('',views.index),
 #   path('', views.student)
#]
urlpatterns = [
    path('', views.student_list, name='student_list'),
]