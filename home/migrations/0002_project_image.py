# Generated by Django 3.0.3 on 2020-06-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
    ]
