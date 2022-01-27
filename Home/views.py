from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic



def home(request):
    return render(request,"home.html")
def survey(request):
    return render(request,"Survey.html")