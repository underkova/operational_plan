from . import views
from django.urls import path
from instructor.views import *


urlpatterns = [
    path('', instructor_list, name='instructor_list'),
    path('list/', list, name='list'),
    # path('', ops, name='plan'),
    # path('detail/<int:pk>/', InstrDetailView.as_view(), name='detail'),
    # path('add/', InstrCreateView.as_view(), name='create'),
    # path('update/<int:pk>', InstrUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', InstrDeleteView.as_view(), name='delete'),
]