# Generated by Django 4.2.20 on 2025-03-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMidiaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('urls', models.URLField(blank=True, help_text='Insira o Link da Rede Social', null=True)),
                ('new_tab', models.BooleanField(default=False)),
                ('site_config', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_config.siteconfig')),
            ],
            options={
                'verbose_name': 'Social Midia Link',
                'verbose_name_plural': 'Social Midia Links',
            },
        ),
    ]
