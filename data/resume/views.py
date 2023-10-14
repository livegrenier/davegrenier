from django.shortcuts import render
from django.http import HttpResponse

from .models import about
from .models import experiance
from .models import skill
from .models import intro
from .models import photo

def index(request):
    abouts = about.objects.all()
    photos = photo.objects.all()
    intros = intro.objects.all()
    experiances = experiance.objects.all()
    skills = skill.objects.all()

    context = {
        'photos':photos, 'abouts':abouts, 'experiances':experiances, 'intros':intros, 'skills':skills
    }

    return render(request, 'index.html', context)
