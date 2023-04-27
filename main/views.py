from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

class HomePage(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-updated')
    template_name = 'index.html'
    paginate_by = 10

