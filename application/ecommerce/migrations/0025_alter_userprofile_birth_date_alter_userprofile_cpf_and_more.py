# Generated by Django 4.2.20 on 2025-04-11 20:06

from django.db import migrations, models
import utils.files.name_file
import utils.validators.validate_cpf
import utils.validators.validate_image


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0024_alter_userprofile_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(help_text='Apenas números, sem pontos ou traços', max_length=11, null=True, validators=[utils.validators.validate_cpf.cpf_validator]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=utils.files.name_file.get_file_name, validators=[utils.validators.validate_image.is_png_svg], verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('EX', 'Estrangeiro')], max_length=2, null=True, verbose_name='Estado'),
        ),
    ]
