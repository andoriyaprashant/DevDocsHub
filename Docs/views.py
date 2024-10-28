from django.shortcuts import render
from .models import ProgrammingLanguage, Documentation,Contact
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages

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


def programming_languages_info(request):
    return render(request, 'programming_languages_info.html')


#code for handling contact us form data
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')

        # You can also add basic validation here if needed
        if name and email and query:
            contact = Contact(name=name, email=email, query=query)
            contact.save()  # Save the contact data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page or a success page
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'html/contact_us.html')
