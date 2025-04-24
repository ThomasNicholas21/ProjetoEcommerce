from django.views.generic import TemplateView
from ecommerce.forms import RegisterForm, UpdateUserForm, ProfileUserForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView
from ecommerce.models.profile_models import UserProfile
# Create your views here.


class BaseProfileView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context.update({
                'user_form': UpdateUserForm(instance=self.request.user),
                'profile_form': ProfileUserForm(instance=self.request.user.profile),
            })
        else:
            context.update({
                'user_form': None,
                'profile_form': None,
            })

        return context



class UserRegisterFormView(BaseProfileView):
    template_name = 'ecommerce/user/register.html'
    success_url = reverse_lazy('ecommerce:index')

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = RegisterForm()
        context.update(
            {
                'user_form': form,
                'profile_form': None
            }
        )
        return render(self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = RegisterForm(self.request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(self.request, user)
            return redirect(self.success_url)

        context.update(
            {
                'user_form': form,
                'profile_form': None
            }
        )

        return render(self.request, self.template_name, context)


class ProfileUserFormView(TemplateView):
    template_name = 'ecommerce/user/update.html'
    success_url = reverse_lazy('ecommerce:update_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_form = UpdateUserForm(instance=self.request.user)
        try:
            profile_form = ProfileUserForm(instance=self.request.user.profile)
        except UserProfile.DoesNotExist:
            profile_form = ProfileUserForm(instance=None)

        context.update(
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )
        return context
    


class UserUpdateFormView(ProfileUserFormView):
    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        user_form = UpdateUserForm(self.request.POST, instance=self.request.user)
        
        try:
            profile = self.request.user.profile
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=self.request.user)
            
        profile_form = ProfileUserForm(
            self.request.POST, 
            self.request.FILES,  # ⚠️ Certifique-se de que FILES está sendo passado!
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()  # Salva o perfil (incluindo a imagem)
            return redirect(self.success_url)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(self.request, self.template_name, context)
    


class AuthenticationLoginFormView(BaseProfileView):
    template_name = 'ecommerce/user/login.html'
    success_url = reverse_lazy('ecommerce:index')

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = AuthenticationForm()
        context.update(
            {
                'user_form': form,
                'profile_form': None
            }
        )

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = AuthenticationForm(self.request, data=self.request.POST)

        if form.is_valid():
            auth.login(self.request, form.get_user())
            return redirect(self.success_url)

        context.update(
            {
                'user_form': form,
                'profile_form': None
            }
        )

        return render(self.request, self.template_name, context)



class LogoutView(RedirectView):
    url = reverse_lazy('ecommerce:index')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super().get(request, *args, **kwargs)
    