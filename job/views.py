from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from company.models import Company
from job.forms import CreateJobForm, UpdateJobForm
from job.models import ApplyJob, Job
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
         
        if request.method == 'POST':
            form = CreateJobForm(request.POST)

            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                print(var.company, var)
                var.save()
                messages.info(request,'Thanks for posting a job circuler !')
                return redirect('dashboard')
            else:
                print("Form errors:", form.errors)
                messages.warning(request,'Something is worng,Try again !')
                return redirect('create_job')
        else:
            form = CreateJobForm()
            context ={'form':form}
            return render(request,'job/create_job.html',context)
    else:
        messages.warning(request,'Your are not allowed to create job')
        return redirect('dashboard')
    
@login_required 
def update_job(request,id):
        if request.user.is_recruiter:
            job = Job.objects.get(id=id)

            if request.method == 'POST':
                form = UpdateJobForm(request.POST,instance=job)

                if form.is_valid():
                    form.save()
                    messages.info(request,'Thanks for updating your post !')
                    return redirect('dashboard')
                else:
                    messages.warning(request,'Something is worng,Try again !')
                    return redirect('create_job')
                
            else:
                form = UpdateJobForm(instance=job)
                context ={'form':form}
                return render(request,'job/create_job.html',context)
        else:
            messages.warning(request,'Your are not allowed to create job')
            return redirect('dashboard')

def manage_job(request):
    jobs = Job.objects.filter(user=request.user,company=request.user.company).order_by('-id')
    context = {
        'jobs':jobs
    }
    return render(request,'job/manage_job.html',context)
@login_required
def apply_to_job(request,id):
    if request.user.has_resume:
        job=Job.objects.get(id=id)
        if ApplyJob.objects.filter(user=request.user,job=id).exists():
            messages.warning(request,'Your already applied to it.')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user=request.user,
                status = 'Pending',
            )
            messages.info(request,'Apply successfull!')
            return redirect('dashboard')
    else:
        messages.warning(request,"Permission denied! You Don't have a resume")
        return redirect('home')
@login_required
def all_applicants(request,id):
    job=Job.objects.get(id=id)
    applicants = ApplyJob.objects.filter(job=job)
    context={
        'applicants':applicants,
        'job':job
    }
    return render(request,'job/all_applicants.html',context)

@login_required
def applied_job(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    return render(request,'job/applied_job.html',{'jobs':jobs})