from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def home_page(request):
    return render(request, 'insanityApp/home_page.html')

def page(request):
    form = PostForm()
    return render(request, 'insanityApp/page.html', {'form': form})

def login(request):
    return render(request, 'insanityApp/login.html', {})

