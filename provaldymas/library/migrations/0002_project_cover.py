# Generated by Django 4.1.2 on 2022-10-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Cover'),
        ),
    ]
