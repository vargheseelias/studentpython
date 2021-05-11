from django.urls import reverse

from empApp.models import Employee
from django.views.generic import TemplateView,ListView,DetailView,CreateView


class IndexView(TemplateView):
    template_name = 'index.html'


class EmployeeCreate(CreateView):
    fields = ("first_name", "last_name", "phn_number")
    model = Employee


class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employee_list'
    template_name = 'empApp/employee_list.html'


class EmployeeDetails(DetailView):
    context_object_name = 'employee_details'
    model = Employee
    template_name = 'empApp/employee_detail.html'
