# Generated by Django 5.0.7 on 2025-01-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_locion_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
