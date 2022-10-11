from django.shortcuts import render, get_object_or_404, redirect

from models_demo.web.models import Employee, Department


def index(request):
    # .filter and .exclude return QUERYSET and are lazy structure - execute later, when needed
    employees = Employee.objects.filter(age=38)
    employees2 = Employee.objects.all()

    # employees2 = Employee.objects.filter(department=2).order_by('age')

    # .get returns a single OBJECT and is eager structure - executes immediately
    department = Department.objects.get(pk=1)

    context = {
        'employees': employees,
        'employees2': employees2
    }

    return render(request, 'index.html', context)


# DELETE a model
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect(index)  # turn back in the previous page, with already deleted employee


# DELETE RESTRICTED - can not procceed, becase  on_delete=models.RESTRICT !!!

def delete_department(request, pk):
    get_object_or_404(Department, pk=pk).delete()


# For the calculated(clickable) url for the object
def department_details(request, pk):
    context = {
        'department': get_object_or_404(Department, pk=pk)
    }
    return render(request, 'departmen_details.html', context)
