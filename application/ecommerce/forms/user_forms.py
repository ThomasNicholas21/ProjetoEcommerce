from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
# forms here

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'email', 'username',
            'password1', 'password2',
        )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu primeiro nome ...'
            },
        ),
        label='Primeiro Nome'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu sobrenome ...'
            },
        ),
        label='Sobrenome'
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu e-mail ...'
            },
        ),
        label='E-mail'
    )


    def clean(self):
        data = super().clean()
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if first_name == last_name:
            msg_first = ValidationError(
                'Primeiro nome deve ser diferente do sobrenome.',
                code='invalid'
            )
            msg_second = ValidationError(
                'Sobrenome deve ser diferent do primeiro nome.',
                code='invalid'
            )
        
            self.add_error('first_name', msg_first)
            self.add_error('last_name', msg_second)

        return data

    def clean_password(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            msg_first = ValidationError(
                'Primeira senha deve ser igual a segunda',
                code='invalid'
            )
            self.add_error('password1', msg_first)
        
        if password2 != password1:
            msg_second = ValidationError(
                'Essa senha não corresponde a primeira.',
                code='invalid'
            )
            self.add_error('password2', msg_second)

        return super().clean()
    
    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')

        if User.objects.filter(email=email):
            msg_error = ValidationError(
                'Já existe uma conta com esse e-mail.',
                code='Invalid'
            )
            self.add_error('email', msg_error)

        return email
