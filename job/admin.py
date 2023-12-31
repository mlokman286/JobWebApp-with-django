from django.contrib import admin

from job.models import *

# Register your models here.
admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(State)
admin.site.register(Industry)