from django.urls import path

from . import views


urlpatterns = [
    path('updateresume',views.update_resume,name='updateresume'),
    path('resume_detail/<str:pk>',views.resume_detail,name='resume_detail'),
]
