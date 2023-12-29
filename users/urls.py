from django.urls import path

from users import views


urlpatterns = [
    path('register_recruiter/',views.register_recruiter,name='register_recruiter'),
    path('register_applicant/',views.register_applicant,name='register_applicant'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
