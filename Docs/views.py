from django.shortcuts import render
from .models import ProgrammingLanguage, Documentation
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

def home(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'home.html', {'languages': languages})

def documentation_list(request, language_id):
    language = ProgrammingLanguage.objects.get(id=language_id)
    docs = Documentation.objects.filter(language=language)
    return render(request, 'docs_list.html', {'language': language, 'docs': docs})

def search_language(request):
    query = request.GET.get('name', '')
    if query:
        languages = ProgrammingLanguage.objects.filter(name__icontains=query)
        if languages.exists():
            language = languages.first()
            return redirect(language.official_website)
    return JsonResponse({'error': 'No programming language found'}, status=404)

def about(request):
    return render(request, 'html/about.html')

def contact(request):
    return render(request, 'html/contact_us.html')

