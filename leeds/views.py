from django import http
from django.shortcuts import render
from django.http import HttpResponse

from .models import Leed
def leed_list(request):
    # return HttpResponse('Hello World')
    leeds = Leed.objects.all()
    context = {
        "leeds": leeds
    }

    return render(request, "leeds/index.html", context) # in leeds templates.

    # return render(request, "index.html", context) # in general templates in setting.

