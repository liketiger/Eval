from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth


from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .models import ClassBlog
from .models import EvalFilter

# Create your views here.

def welcome(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            return render(request, 'classcrud/classblog_home.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'classcrud/classblog_home.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'classcrud/classblog_signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('welcome')
        else:
            return render(request, 'classcrud/classblog_signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'classcrud/classblog_signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('welcome')
    return render(request, 'classcrud/classblog_signup.html')

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