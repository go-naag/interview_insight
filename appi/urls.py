from django.urls import path,include
from . import views


urlpatterns = [
    path('home/',views.home_html,name='home'),
    path('form/',views.form_html,name='form'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('',views.login,name='login'),
    
]