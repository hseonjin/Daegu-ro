from django.urls import path
from . import views

# app_name = 'recommend'

urlpatterns = [
    # http://127.0.0.1:8000/recommend
    path('', views.recommend, name='recommend'),

]