from django.shortcuts import redirect, render
from django.contrib import messages
from job.models import ApplyJob, Job
from website.filter import JobFilter

# Create your views here.
def home(request):
    filter = JobFilter(request.GET, queryset = Job.objects.filter(is_available = True).order_by('-published'))
    # jobs = Job.objects.all().order_by('-id')
    context={'filter':filter}
    return render(request,'website/home.html',context)

def job_list(request):
    jobs = Job.objects.filter(is_available=True).order_by('-published')
    context={'jobs':jobs}
    return render(request,'website/joblist.html',context)

def job_details(request,id):
    if request.user.is_authenticated:
        if ApplyJob.objects.filter(user=request.user,job=id).exists():
            has_applied = True
        else:
            has_applied = False
        
        job = Job.objects.get(id=id)
        context={
            'job':job,
            'has_applied':has_applied
        }
        return render(request,'website/job_details.html',context)
    else:
        messages.warning(request,'Login first then continue again !')
        return redirect('login')
    
def job_search(request):
    query= request.GET['search']
    jobs = Job.objects.filter(title__icontains = query)
    return render(request,'website/joblist.html',{'jobs':jobs})