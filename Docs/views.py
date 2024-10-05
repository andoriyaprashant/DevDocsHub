from django.http import HttpResponse
from django.shortcuts import render
from .models import ProgrammingLanguage, Documentation

def home(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'home.html', {'languages': languages})

def documentation_list(request, language_id):
    language = ProgrammingLanguage.objects.get(id=language_id)
    docs = Documentation.objects.filter(language=language)
    return render(request, 'docs_list.html', {'language': language, 'docs': docs})

def docs_list(request):
    return HttpResponse(request,"You are on docs_list page.")
