from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('account/', views.account_info, name='account_info'),
     path('register/', views.register, name='register'),
]