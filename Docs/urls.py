from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('language/', views.documentation_list, name='documentation_list'),
    path('add_documentation/',views.add_documentation,name='add'),
    path('add/language/',views.Add_languages,name='add_language'),
]

