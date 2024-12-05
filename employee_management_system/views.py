from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse,HttpResponseRedirect
from django.template import loader
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all().values()  
    context = {'employees': list(employees)}
    return render(request, 'employees/employee_list.html', context)

 
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/employee_create.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_update.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        try:
            employee.delete()
            return JsonResponse({ 'success': True })
        except Exception as e:
            return JsonResponse({ 'success': False, 'error': str(e) }, status=500)
    return JsonResponse({ 'success': False, 'error': 'Method not allowed' }, status=405)

