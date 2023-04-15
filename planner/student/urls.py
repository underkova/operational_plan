from django.urls import path
from student.views import *



urlpatterns = [
    path('', ops, name='plan'),
    path('list/', list, name='list'),
    path('detail/<int:pk>/', StudDetailView.as_view(), name='detail'),
    path('add/', StudCreateView.as_view(), name='create'),
    path('update/<int:pk>', StudUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', StudDeleteView.as_view(), name='delete'),
]