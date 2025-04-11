from django.db import models
from utils.files.name_file import get_file_name
from utils.images.image_validator import resize_image
from utils.validators.validate_image import is_png_svg
from django.contrib.auth.models import User


class UserProfileAdress(models.Model):
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    street = models.CharField(
        max_length=255, 
        blank=False, 
        null=True,
        verbose_name='Rua'
        )
    number = models.CharField(
        max_length=10, 
        blank=False, 
        null=True,
        verbose_name='Número'
        )
    neighborhood = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
        verbose_name='Bairro'
        )
    city = models.CharField(
        max_length=100, 
        blank=False, 
        null=True,
        verbose_name='Cidade'
        )
    zip_code = models.CharField(
        max_length=10, 
        blank=False, 
        null=True,
        verbose_name='CEP'
        )
    complement = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.street + ' ' + self.number + ', ' + self.neighborhood + ', ' + self.city + ', ' + self.zip_code


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to=get_file_name, 
        blank=True, 
        null=True,
        validators=[is_png_svg], 
        )
    cpf = models.CharField(
        max_length=14, 
        blank=False, 
        null=True
        )
    phone = models.CharField(
        max_length=15, 
        blank=False, 
        null=True
        )
    birth_date = models.DateField(
        blank=True, 
        null=True
        )
    address = models.OneToOneField(
        UserProfileAdress, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='address',
        verbose_name='Endereço'
        )
    state = models.CharField(
        max_length=2,
        choices=(
                    ('AC', 'Acre'), 
                    ('AL', 'Alagoas'), 
                    ('AP', 'Amapá'), 
                    ('AM', 'Amazonas'),
                    ('BA', 'Bahia'), 
                    ('CE', 'Ceará'), 
                    ('DF', 'Distrito Federal'), 
                    ('ES', 'Espírito Santo'),
                    ('GO', 'Goiás'), 
                    ('MA', 'Maranhão'), 
                    ('MT', 'Mato Grosso'), 
                    ('MS', 'Mato Grosso do Sul'),
                    ('MG', 'Minas Gerais'), 
                    ('PA', 'Pará'), 
                    ('PB', 'Paraíba'), 
                    ('PR', 'Paraná'),
                    ('PE', 'Pernambuco'), 
                    ('PI', 'Piauí'), 
                    ('RJ', 'Rio de Janeiro'), 
                    ('RN', 'Rio Grande do Norte'),
                    ('RS', 'Rio Grande do Sul'), 
                    ('RO', 'Rondônia'), 
                    ('RR', 'Roraima'), 
                    ('SC', 'Santa Catarina'),
                    ('SP', 'São Paulo'), 
                    ('SE', 'Sergipe'), 
                    ('TO', 'Tocantins'),
                    ('EX', 'Estrangeiro'),
                ), 
                blank=True, 
                null=True
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        current_profile_picture_name = str(self.profile_picture.name)
        super_save = super().save(*args, **kwargs)
        profile_picture_changed = False

        if self.profile_picture:
            profile_picture_changed = current_profile_picture_name != self.profile_picture.name
        
        if profile_picture_changed:
            resize_image(self.profile_picture)

        return super_save
    
    def __str__(self):
        return self.user.username
    