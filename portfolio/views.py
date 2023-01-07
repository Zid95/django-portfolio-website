from django.shortcuts import render
from .models import *


def index(request):
    data_profile = Self.objects.all()
    data_about = About.objects.all()
    data_facts = Facts.objects.all()
    data_skills = Skills.objects.all()

    context = {
        'profile': data_profile,
        'about': data_about,
        'facts': data_facts,
        'skills': data_skills,
    }
    return render(request, 'index.html', context)
