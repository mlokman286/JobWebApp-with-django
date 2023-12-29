from django.urls import path

from job import views


urlpatterns = [
    path('create_job/',views.create_job,name='create_job'),
    path('update_job/<str:id>',views.update_job,name='update_job'),
    path('manage_job/',views.manage_job,name='manage_job'),
    path('apply-to-job/<int:id>',views.apply_to_job,name='apply-to-job'),
    path('all_applicants/<int:id>',views.all_applicants,name='all_applicants')
]
