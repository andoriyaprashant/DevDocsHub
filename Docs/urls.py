from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('language/<int:language_id>/', views.documentation_list, name='documentation_list'),
    path('search/', views.search_language, name='search_language'),
]

