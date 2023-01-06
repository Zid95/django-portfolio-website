from django.shortcuts import render
from .models import *


def index(request):
    data_profile = Self.objects.all()
    data_about = About.objects.all()

    context = {
        'profile': data_profile,
        'about': data_about,
    }
    return render(request, 'index.html', context)
