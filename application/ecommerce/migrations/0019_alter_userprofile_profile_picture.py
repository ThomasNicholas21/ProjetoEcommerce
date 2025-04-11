# Generated by Django 4.2.20 on 2025-04-11 15:13

from django.db import migrations, models
import utils.files.name_file
import utils.validators.validate_image


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_alter_userprofile_options_alter_userprofile_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=utils.files.name_file.get_file_name, validators=[utils.validators.validate_image.is_png_svg]),
        ),
    ]
