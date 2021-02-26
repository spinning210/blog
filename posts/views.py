from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def covid19_world_map(request):
    return render(request, 'posts/covid19_world_map.html')