from django.shortcuts import redirect, render
from django.contrib import messages
from company.forms import UpdateCompanyForm
from company.models import Company
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateCompanyForm(request.POST,instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info(request,'Your company is now active. Now start createing jobs, Good luck !')
                return redirect('dashboard')
            else:
                print('Erorrs:',form.errors)
                messages.warning(request,'something went wrong')
                return redirect('updatecompany')
        else:
            form= UpdateCompanyForm(instance=company)
            context = {
                'form':form,
            }
            return render(request,'company/updatecompany.html',context)
    else:
        messages.warning(request,('Permission Denied !'))
        return redirect('dashboard')
    
@login_required
def company_detail(request,id):
    company=Company.objects.get(id=id)
    context ={
        'company':company
    }
    return render(request,'company/company_detail.html',context)