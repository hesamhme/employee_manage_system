from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
import requests
from .forms import PenaltyForm

from .models import Employee

class EmpListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = 'employee/list_view.html'
    context_object_name = 'emp'


class NewEmp(LoginRequiredMixin, generic.CreateView):
    model = Employee
    fields = ['phon_number','first_name','last_name','position','cover','salary', 'manager']
    template_name = 'employee/new_emp.html'


class DelEmp(LoginRequiredMixin, generic.DeleteView, UserPassesTestMixin):
    model = Employee
    template_name = 'employee/delete_view.html'
    success_url = reverse_lazy('home')


    def test_func(self):
        obj = self.get_object()
        return obj


class EditEmp(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Employee
    fields = ['phon_number','first_name','last_name','position','cover','salary', 'manager']
    template_name = 'employee/edit_emp.html'


    def test_func(self):
        obj = self.get_object()
        return obj


class PenaltyEmployee(LoginRequiredMixin, UserPassesTestMixin, generic.View):
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        penalty_amount = int(request.POST.get('penalty_amount'))
        employee.salary -= penalty_amount
        employee.save()
        employee_phone_number = employee.phon_number
        api_key ='some_api_key'
        url = '#/%s/# %api_key
        pay_load = {
                'sender' : '#',
                'receptor': employee_phone_number,
                'message': f'you hot penalty this much!! {penalty_amount} '
            }
        res = requests.post(url, data = pay_load)
        return redirect('home')

    def test_func(self):
        # Add your authorization logic here if needed
        return True


class RewardEmployee(LoginRequiredMixin, UserPassesTestMixin, generic.View):
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        reward_amount = int(request.POST.get('reward_amount'))
        employee.salary += reward_amount
        employee.save()
        employee_phone_number = employee.phon_number
       api_key ='some_api_key'
        url = '#/%s/# %api_key
        pay_load = {
                'sender' : '#',
                'receptor': employee_phone_number,
                'message': f' you got reward this much!! {reward_amount}'
            }
        res = requests.post(url, data = pay_load)
        return redirect('home')

    def test_func(self):
        return True
