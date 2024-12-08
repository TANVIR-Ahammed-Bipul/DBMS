from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import joined_view

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_file, name='upload'),
    path('items/', views.item_list, name='item_list'),  # Corrected this path
    path('items/new/', views.create_item, name='create_item'),
    path('items/<int:pk>/edit/', views.update_item, name='update_item'),
    path('items/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('', views.home, name='home'),  # Default route for home
    path('joined/', joined_view, name='joined_view'),
]

