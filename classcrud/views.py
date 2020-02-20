from django.shortcuts import render
from django.utils import timezone


from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .models import ClassBlog
from .models import EvalFilter

# Create your views here.

def welcome(request):
    return render(request, 'classcrud/classblog_home.html')

class BlogView(FilterView):
    model = ClassBlog
    context_object_name = 'evals'
    filterset_class = EvalFilter

class BlogCreate(CreateView):
    model = ClassBlog    
    fields = ['강의명', '교수명', '평가내용']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):
    model = ClassBlog

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['강의명', '교수명', '평가내용']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')