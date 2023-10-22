from django.contrib import admin
from django.urls import path, include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', views.login_page, name='login_page'),
    path('home/', views.home_page, name='home_page'),
    path('register/', views.register_page, name='register_page')
]
