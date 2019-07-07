from django.shortcuts import render
from .models import Blog, Portfolio
# Create your views here.

def home(request):
    blog = Blog.objects
    portfolio = Portfolio.objects
    return render(request, 'home.html', {'blog': blog, 'portfolio':portfolio})