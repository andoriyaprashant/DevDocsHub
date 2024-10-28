from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('language/<int:language_id>/', views.documentation_list, name='documentation_list'),
    path('search/', views.search_language, name='search_language'),
    path('programming_languages_info/', views.programming_languages_info, name='programming_languages_info'),
    path('open_source.html', views.open_source, name='open_source'), 
    path('Tut_Guides.html', views.Tut_Guides, name='Tut_Guides'),
]
