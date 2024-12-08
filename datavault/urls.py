from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.admin import admin_site


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('core.urls')),  # Include the core app's URLs
    path('admin/', admin_site.urls),  # Use custom admin site
    path('', include('core.urls')),  # Include your app's URLs
]
