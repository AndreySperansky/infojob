from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from .forms import *
from .models import *
# from django.db import transaction
# from django.http import HttpResponse



class HomepageView(TemplateView):
    template_name = "employer/employer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.order_by('id')
        context['vacancy'] = Vacancy.objects.order_by('id')
        return context


#############################################################################################
#             Companies Views
#############################################################################################


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'employer/company_detail.html'



class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'employer/company_create.html'
    fields = ['company_name', 'industry_name', 'logo_pic', 'email', 'site_link', 'is_active']
    success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employer:company_detail', kwargs={'pk': self.object.pk})


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = 'employer/company_update.html'
    fields = ['company_name', 'industry_name', 'logo_pic', 'email', 'site_link', 'is_active']
    success_url = None

    def get_success_url(self):
        return reverse_lazy('employer:company_detail', kwargs={'pk': self.object.pk})


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    context_object_name = 'company'
    template_name = 'employer/confirm_delete.html'
    success_url = reverse_lazy('employer:employer')



#############################################################################################
#             Companies Views
#############################################################################################


class VacancyDetail(LoginRequiredMixin, DetailView):
    model = Vacancy
    context_object_name = 'vacancy'
    template_name = 'employer/vacancy_detail.html'



class VacancyCreate(LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'employer/vacancy_create.html'
    fields = ['company', 'position', 'city', 'duties', 'compensation', 'is_active']
    success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VacancyCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employer:vacancy_detail', kwargs={'pk': self.object.pk})


class VacancyUpdate(LoginRequiredMixin, UpdateView):
    model = Vacancy
    template_name = 'employer/vacancy_update.html'
    fields = ['company', 'position', 'city', 'duties', 'compensation', 'is_active']
    success_url = None

    def get_success_url(self):
        return reverse_lazy('employer:vacancy_detail', kwargs={'pk': self.object.pk})


class VacancyDelete(LoginRequiredMixin, DeleteView):
    model = Vacancy
    context_object_name = 'vacancy'
    template_name = 'employer/confirm_delete.html'
    success_url = reverse_lazy('employer:employer')