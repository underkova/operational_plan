from . import views
from django.urls import path
from instructor.views import *


urlpatterns = [
    path('', instructor_list, name='home'),
    path('list/', list, name='list'),
    path('detail/<int:pk>/', InstrDetailView.as_view(), name='detail'),
    path('add/', InstrAddStud.as_view(), name='add'),
    path('update/<int:pk>', InstrUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', InstrDeleteView.as_view(), name='delete'),
]