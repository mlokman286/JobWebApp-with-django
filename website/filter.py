import django_filters
from job.models import Job

class JobFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    location=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title','location','job_type']