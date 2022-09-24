from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse("<h1>Home page")

def about_view(request):
    return HttpResponse("<h1>About page")

def contact_view(request):
    return HttpResponse("<h1>Contact page")