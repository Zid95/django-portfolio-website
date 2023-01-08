from django.shortcuts import render ,redirect
from django.core.mail import send_mail 
from django.template.loader import render_to_string
from .models import *
from .forms import *


def index(request):

    form = ContactForm()
    data_profile = Self.objects.all()
    data_about = About.objects.all()
    data_facts = Facts.objects.all()
    data_skills = Skills.objects.all()
    data_resume = Resume.objects.all()
    data_resume1 = Resume1.objects.all()
    data_resume2 = Resume2.objects.all()
    data_resume3 = Resume3.objects.all()
    data_resume4 = Resume4.objects.all()
    data_service = Services.objects.all()
    

    context = {
        'profile': data_profile,
        'about': data_about,
        'facts': data_facts,
        'skills': data_skills,
        'resume': data_resume,
        'resume1': data_resume1,
        'resume2': data_resume2,
        'resume3': data_resume3,
        'resume4': data_resume4,
        'services': data_service,
        'form':form,
    }
    return render(request, 'index.html', context)


