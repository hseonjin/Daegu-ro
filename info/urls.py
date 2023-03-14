from django.urls import path
from . import views

# app_name = 'info'

urlpatterns = [
    # http://127.0.0.1:8000/info
    path('', views.profile, name='profile'),

]