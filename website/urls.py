from django.urls import path

from website import views


urlpatterns = [
    path('',views.home,name='home'),
    path('job_list',views.job_list,name='job_list'),
    path('job_details/<str:id>',views.job_details,name='job_details')
]
