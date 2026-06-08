from django.shortcuts import render,HttpResponse
from .models import reg

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def registration(request):   # changed name
    return render(request,"reg.html")

def saveform(request):
    if request.method=="POST":
        n=request.POST.get("name")
        em=request.POST.get("email")
        ps=request.POST.get("password")
        cn=request.POST.get("contact")
        ad=request.POST.get("address")

        r=reg(
            name=n,
            email=em,
            password=ps,
            contact=cn,
            address=ad
        )
        r.save()

        return HttpResponse("Registration completed successfully")

    else:
        return HttpResponse("Failed")
    
    

def viewstudent(request):
    data=reg.objects.all().order_by('-id')
    return render(request,"viewstudent.html",{'data':data})


def updatestudent(request):
    id=request.GET["id"]
    data=student.object.filter(id=id)
    
    return render(request,"updatestudent.html")