from django.shortcuts import render
from .forms import StudForm
from .models import Student

# Create your views here.
def getHome(request):
    return render(request,"studApp/home.html")
def registration(request):
    if request.method=='GET':
        frm=StudForm()
        return render(request,'studApp/register.html',{'form':frm})#context-object pass
    # else:
    #     na=request.POST.get("sname")
    #     adr=request.POST.get("addr")
    #     pn=request.POST.get("phn")
    #     crs=request.POST.get("course")
    #     try:
    #         obj=Student(name=na,address=adr,)

