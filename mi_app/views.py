from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PageForm, SignUpForm, CustomLoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def home(request):
    return render(request, 'home.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

@login_required
def page_new(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'page_edit.html', {'form': form})

@login_required
def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'page_edit.html', {'form': form})

@login_required
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('page_list')
    return render(request, 'page_confirm_delete.html', {'page': page})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page_detail.html', {'page': page})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomLoginForm()

    return render(request, 'custom_login.html', {'form': form})

def about_me(request):
    return render(request, 'about_me.html')