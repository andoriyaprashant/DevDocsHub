from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('language/<int:language_id>/', views.documentation_list, name='documentation_list'),
    path('search/', views.search_language, name='search_language'),
    path('programming_languages_info/', views.programming_languages_info, name='programming_languages_info'),
]
