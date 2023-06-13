from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout,name='logout'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('', views.dashboard,name='dashboard'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]