from django.urls import path

from company import views


urlpatterns = [
    path('updatecompany',views.update_company,name='updatecompany'),
    path('company_detail/<str:id>',views.company_detail,name='company_detail')
]
