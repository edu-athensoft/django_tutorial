from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
    html_str = "view: login"
    return HttpResponse(html_str)