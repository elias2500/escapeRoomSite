from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegisterForm

# Create your views here.

class RegisterView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm