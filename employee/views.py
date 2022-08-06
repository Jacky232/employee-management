from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def home(request):
    emp = Employee.objects.all()
    return render(request,"employee/home.html",{'emp':emp})



def emp_add(request):
    if request.method=="POST":
        print("Added")
        #Get the user input
        emp_id=request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_email=request.POST.get("emp_email")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        
        #Create an object for models
        e = Employee()
        e.idnum=emp_id
        e.name=emp_name
        e.email=emp_email
        e.phone=emp_phone
        e.address=emp_address
        e.save()
        return redirect("/employee/home")
        
    return render(request,"employee/add_employee.html",{})


def emp_delete(request,idnum):
    e=Employee.objects.get(pk=idnum)
    e.delete()
    return redirect("/employee/home")

def emp_update(request,idnum):
    emp=Employee.objects.get(pk=idnum)
    return render(request,"employee/update_employee.html",{'emp':emp})

def do_emp_update(request,idnum):
    emp_idnum=request.POST.get('emp_idnum')
    emp_name=request.POST.get('emp_name')
    emp_email=request.POST.get('emp_email')
    emp_phone=request.POST.get('emp_phone')
    emp_address=request.POST.get('emp_address')
    
    emp=Employee.objects.get(pk=idnum)
    
    emp.idnum=emp_idnum
    emp.name=emp_name
    emp.email=emp_email
    emp.phone=emp_phone
    emp.address=emp_address
    
    emp.save()
    
    return redirect("/employee/home")
    