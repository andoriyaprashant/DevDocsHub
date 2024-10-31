from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('language/<int:language_id>/', views.documentation_list, name='documentation_list'),
    path('search/', views.search_language, name='search_language'),
    path('playground/',views.playground,name = 'playground'),
]

