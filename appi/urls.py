from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns = [
    path('home/',views.home_html,name='home'),
    path('form/',views.form_html,name='form'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('',views.login,name='login'),
    path('add_interview/', views.add_interview, name='add_interview'),
    path('companies/',views.companies,name='companies'),
    path('company/<str:company_name>/<int:year>/', views.company_detail, name='company_detail'),
    path('year_of_passouts/<str:company_name>/', views.year_of_passouts, name='year_of_passouts'),
    path('user-detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('search/', views.search_companies, name='search_companies'),
    path('search_company_students_home/',views.search_company_students_home,name='search_company_students_home'),
    path('community/',views.community,name='community'),
    path('admin/', admin.site.urls),
    path('community/',views.community,name='community'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
    path('addInDiscussion/<int:topic_id>/', views.addInDiscussion, name='addInDiscussion'),
    path('archive/',views.archive, name = 'archive'),

    path('interview_statistics', views.interview_statistics, name='interview_statistics'),
]