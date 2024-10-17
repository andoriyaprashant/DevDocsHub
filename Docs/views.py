from django.shortcuts import render
from django.views.generic import ListView
from .models import ProgrammingLanguage, Documentation
from django.http import HttpResponse
from django.template import loader

class DocsListView(ListView):
    model = Documentation
    template_name = 'docs_list.html'  # Adjust the template path as needed
    context_object_name = 'documents'  # This will be available in the template

    
def home(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'home.html', {'languages': languages})

def documentation_list(request, language_id):
    language = ProgrammingLanguage.objects.get(id=language_id)
    docs = Documentation.objects.filter(language=language)
    return render(request, 'docs_list.html', {'language': language, 'docs': docs})

def languages(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'languages.html', {'languages': languages})


def about_view(request):
    return render(request, 'about.html')  # Adjust the template name as needed

def contact_view(request):
    return render(request, 'contact.html') 