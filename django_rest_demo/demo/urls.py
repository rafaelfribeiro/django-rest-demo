from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name="clients"),
    path('detail/<str:pk>/', views.client_detail, name="detail"),
    path('create', views.client_create, name="create"),
    path('update/<str:pk>/', views.client_update, name="update"),
    path('delete/<str:pk>/', views.client_delete, name="delete"),
]