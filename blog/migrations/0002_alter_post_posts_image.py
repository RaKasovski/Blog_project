# Generated by Django 4.0.4 on 2022-06-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posts_image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]