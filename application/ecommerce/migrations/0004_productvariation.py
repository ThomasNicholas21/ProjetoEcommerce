# Generated by Django 4.2.20 on 2025-03-24 16:40

from django.db import migrations, models
import django.db.models.deletion
import utils.validators.validate_image


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('product_image', models.ImageField(blank=True, default=None, upload_to='products/%Y/%m', validators=[utils.validators.validate_image.is_png_svg])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promotional_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(default=0, help_text='Coloque quantos produtos tem em estoque.')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
            options={
                'verbose_name': 'Variation',
                'verbose_name_plural': 'Variations',
            },
        ),
    ]
