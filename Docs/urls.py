from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/', views.docs_list, name='docs_list'),
    path('language/<int:language_id>/', views.documentation_list, name='documentation_list'),
]

