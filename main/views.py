from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()
        context['universities'] = University.objects.all()
        return context


class SchoolsListView(ListView):
    model = School
    queryset = School.objects.order_by('-id')
    template_name = 'schools.html'
    paginate_by = 3


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school-details.html'
    context_object_name = 'school'


class SchoolCreateView(CreateView):
    form_class = AddSchoolForm
    template_name = 'schools-add.html'
    success_url = reverse_lazy('main')


class UniversityListView(ListView):
    model = University
    queryset = University.objects.order_by('-id')
    template_name = 'university.html'
    paginate_by = 3


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university-details.html'
    context_object_name = 'university'


class UniversityCreateView(CreateView):
    form_class = AddUniversityForm
    template_name = 'university-add.html'
    success_url = reverse_lazy('main')



