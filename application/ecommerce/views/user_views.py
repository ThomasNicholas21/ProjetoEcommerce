from django.shortcuts import render
from django.views.generic.edit import FormView
from ecommerce.forms import RegisterForm
from django.urls import reverse_lazy
# Create your views here.

def user_register(request):
    return render(request, 'ecommerce/user/register.html') 

class UserRegisterFormView(FormView):
    template_name = 'ecommerce/user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
