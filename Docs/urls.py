from django.urls import path
from .views import home, languages, documentation_list, DocsListView, about_view, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('language/<int:language_id>/', documentation_list, name='documentation_list'),
    path('languages/', languages, name='languages'),  # Page to list programming languages
    path('docs/', DocsListView.as_view(), name='docs_list'),  # Docs list page
    path('about/', about_view, name='about'),  # Add this line for the about view
    path('contact/', contact_view, name='contact'),# Add this line for the contact view
]