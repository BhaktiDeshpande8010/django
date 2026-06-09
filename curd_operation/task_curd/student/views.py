from django.shortcuts import render,HttpResponse,redirect
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


def deletestudent(request,id):
    reg.objects.filter(id=id).delete()
    
    return redirect("/viewstudent")
    
# def deletestudent(request):
#     id=request.GET["id"]
#     reg.objects.filter(id).delete() 
#     return redirect("/viewstudent")


# def updatestudent(request, id):
#     id=request.GET["id"]
#     data=reg.objects.filter(id=id).update()
    
#     return render(request,"updatestudent.html")

def updatestudent(request, id):
    data = reg.objects.get(id=id)

    return render(request, "updatestudent.html", {"i": data})          #chagpt code


def profileupdate(request):
    if request.method=="POST":
        id=request.POST["id"]
        n=request.POST.get("name")
        em=request.POST.get("email")
        ps=request.POST.get("password")
        cn=request.POST.get("contact")
        ad=request.POST.get("address")

        r=reg.objects.filter(id=id).update(
            name=n,
            email=em,
            password=ps,
            contact=cn,
            address=ad
        )

        # return HttpResponse("Profile Updated successfully")
        return redirect("viewstudent")
    else:
        return HttpResponse("Failed")
    
  
  
def login(request):  
    return render(request,"login.html")


def logincheck(request):
    if request.method == "POST":
        em = request.POST["email"]
        ps = request.POST["password"]

        # FIXED: proper check
        if reg.objects.filter(email=em, password=ps).exists():
            return redirect("/dashboard")
        else:
            return redirect("/login")

    return HttpResponse("failed")


def dashboard(request):
    return render(request, "dashboard.html")


def logout(request):
    return redirect("/login")
    