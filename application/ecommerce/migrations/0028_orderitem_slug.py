# Generated by Django 4.2.20 on 2025-05-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0027_remove_order_totol_items_order_total_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
