from django.shortcuts import render
from .models import *


def index(request):
    data_profile = Self.objects.all()

    context = {
        'profile': data_profile,
    }
    return render(request, 'index.html', context)
