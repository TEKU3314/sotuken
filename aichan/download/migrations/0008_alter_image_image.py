# Generated by Django 4.1.3 on 2023-01-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]