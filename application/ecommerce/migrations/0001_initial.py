# Generated by Django 4.2.20 on 2025-03-22 22:47

from django.db import migrations, models
import utils.validators.validate_image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('short_description', models.CharField(max_length=128)),
                ('long_description', models.TextField()),
                ('product_image', models.ImageField(blank=True, default='', upload_to='products/%Y/%m', validators=[utils.validators.validate_image.is_png_svg])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promotional_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_type', models.CharField(choices=[('S', 'Simples'), ('V', 'Variável')], default=None, help_text='Produto "Simples" não possui variações, sendo ele único. Já o produto "Variável" é um produto cujo possui variações, por exemplo, cores e tamanhos diferentes.', max_length=1)),
                ('stock', models.IntegerField(default=0, help_text='Coloque quantos produtos tem em estoque.')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
