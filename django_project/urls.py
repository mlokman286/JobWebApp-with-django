from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('website.urls')),
    path('accounts/',include('users.urls')),
    path('company/',include('company.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('resume/',include('resume.urls')),
    path('job/',include('job.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls'))
]
