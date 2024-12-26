from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/<int:pk>/edit/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('profile/<int:profile_pk>/project/create/', views.project_create, name='project_create'),
    path('profile/<int:profile_pk>/project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('profile/<int:profile_pk>/project/<int:pk>/delete/', views.project_delete, name='project_delete'),
]
