from django.views.generic.edit import FormView
from ecommerce.forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# Create your views here.


class UserRegisterFormView(FormView):
    template_name = 'ecommerce/user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form: RegisterForm):
        form.save()
        return super().form_valid(form)


class AuthenticationFormView(FormView):
    template_name = 'ecommerce/user/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form: AuthenticationForm):
        user = form.get_user()
        auth.login(request=self.request, user=user)
        return super().form_valid(form)
