from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard.html')
# def proxy(requset):
#     if requset.user.is_applicant:
#         return redirect('applicant-dashboard')
#     elif requset.user.is_applicant:
#         return redirect('recruiter-dashboard')
#     else:
#         return redirect('login')
    
# def applicant_dashboard(request):
#     return render(request,'dashboard/applicant_dashboard.html')

# def recruiter_dashboard(request):
#     return render(request,'dashboard/recruiter_dashboard.html')