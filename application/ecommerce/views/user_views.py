from django.views.generic.edit import FormView
from ecommerce.forms import RegisterForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views.generic.base import RedirectView
# Create your views here.


class UserRegisterFormView(FormView):
    template_name = 'ecommerce/user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form: RegisterForm):
        form.save()
        return super().form_valid(form)


class UserUpdateFormView(FormView):
    template_name = 'ecommerce/user/update.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('ecommerce:update_user')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(instance=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class AuthenticationLoginFormView(FormView):
    template_name = 'ecommerce/user/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form: AuthenticationForm):
        user = form.get_user()
        auth.login(self.request, user)
        return super().form_valid(form)



class LogoutView(RedirectView):
    url = reverse_lazy('ecommerce:index')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super().get(request, *args, **kwargs)
    