# Generated by Django 4.2.17 on 2025-01-14 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uid',
            new_name='userid',
        ),
    ]
