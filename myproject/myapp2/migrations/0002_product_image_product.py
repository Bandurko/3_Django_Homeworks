# Generated by Django 5.0.3 on 2024-04-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_product',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
