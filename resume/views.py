from django.shortcuts import redirect, render
from resume.forms import UpdateResumeForm
from django.contrib import messages
from resume.models import Resume
from users.models import User

# Create your views here.
def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                var = form.save(commit = False)
                user=User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()
                messages.info(request,'Your new resume has been created. Now apply for jobs!')
                return redirect('dashboard')
            else:
                messages.warning(request,'Something went wrong')
                return redirect('updateresume')
        else:
            form = UpdateResumeForm(instance=resume)
            context = {'form':form}
            return render(request,'resume/resumeupdate.html',context)
    else:
        messages.warning(request,'Permission Denied !')


def resume_detail(request,pk):
    resume = Resume.objects.get(id=pk)
    context ={ 'resume':'resume'}
    return render(request,'resume/resume_detail.html',context)