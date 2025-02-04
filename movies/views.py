from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import ReviewForm

