from django.urls import path
from . import views

# app_name = 'list'

urlpatterns = [
    # http://127.0.0.1:8000/list
    path('', views.list, name='list'),

    # healing
    path('list_healing/', views.list_healing, name='list_healing'),

    # history
    path('list_history/', views.list_history, name='list_history'),

    # food
    path('list_food/', views.list_food, name='list_food'),

    #hotplace
    path('list_hotplace/', views.list_hotplace, name='list_hotplace'),

    # experience
    path('list_experience/', views.list_experience, name='list_experience'),

    # activity
    path('list_activity/', views.list_activity, name='list_activity'),

    # shoping
    path('list_shoping/', views.list_shoping, name='list_shoping'),

    # culture
    path('list_culture/', views.list_culture, name='list_culture'),

    # night
    path('list_night/', views.list_night, name='list_night'),

    # child
    path('list_child/', views.list_child, name='list_child'),

]