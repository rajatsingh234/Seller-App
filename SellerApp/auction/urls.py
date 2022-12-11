from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.create_auction),
    path('api', views.ApiOverview),
    path('all/', views.view_model),
    path('create', views.create_model),
    path('delete/<int:pk>', views.delete_model),
    path('update/<int:pk>', views.update_model),

]
