from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.contrib.auth import password_validation
# forms here

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'email', 'username',
            'password1', 'password2',
        )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu usuário ...'
            }
        ),
        label='Usuário',
        required=True,
        help_text=mark_safe(
                "Use apenas caracteres alfanuméricos e os seguintes símbolos: @ . + - _<br>"
                "Exemplos válidos: nome.sobre+nome@exemplo.com, usuario_123"
        )
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
        label='E-mail',
        required=True
    )

    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Insira sua senha ...',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirme sua senha ...',
            }
        ),
        strip=False,
        help_text=('Coloque a mesma senha de antes, para verificação.'),
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
