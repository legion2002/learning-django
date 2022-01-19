from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# This is a request handler


def trial_func(request):
    return HttpResponse("Wazzzupppp")
