from django.shortcuts import render
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

def page_new(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page_list') 
    else:
        form = PageForm()
    return render(request, 'page_edit.html', {'form': form})

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