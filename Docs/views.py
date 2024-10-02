from django.shortcuts import render,redirect
from .models import ProgrammingLanguage, Documentation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def home(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'home.html', {'languages': languages})

def documentation_list(request):
    language = ProgrammingLanguage.objects.all()
    docs = Documentation.objects.all()
    if request.method=="POST":
        got_language = request.POST.get('language','')
        if language:
            sort_language = ProgrammingLanguage.objects.filter(name=got_language).first()

            if sort_language:
                docs = Documentation.objects.filter(language=sort_language)
    
    context={
        'language': language,
        'docs': docs
    }
    return render(request, 'docs_list.html',context)


def add_documentation(request):
    if request.method == 'POST':
        p_language = request.POST.get('language', '')
        doc_title = request.POST.get('doc_title', '')
        content = request.POST.get('content', '')
        doc_url = request.POST.get('url', '')


        try:
            language = ProgrammingLanguage.objects.get(name=p_language)
            Documentation.objects.create(
                language=language,
                doc_title=doc_title,
                content=content,
                doc_url=doc_url
            )
            return redirect('home')

        except ObjectDoesNotExist:
            return render(request, 'error.html', {'error': 'Programming language not found'})
        
    all_language=ProgrammingLanguage.objects.all()

    context={
        'all_language':all_language,
    }
    return render(request, 'Add_documentation.html',context)



def Add_languages(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        official_website = request.POST.get('url', '')
        description = request.POST.get('content', '')
        
        try:
            ProgrammingLanguage.objects.create(
                name=name,
                official_website=official_website,
                description=description
            )
            messages.success(request, "Programming language added successfully!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    
    return render(request, 'Add_language.html')
