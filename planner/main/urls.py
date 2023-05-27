from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='main'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
