from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm  # Import your custom form

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # specify your template here



class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:login'))  # Redirect to login after successful registration
        return render(request, 'accounts/register.html', {'form': form})
