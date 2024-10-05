from django.urls import path
from .views import CustomLoginView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
