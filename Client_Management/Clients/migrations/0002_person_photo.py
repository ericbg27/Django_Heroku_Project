# Generated by Django 2.2.1 on 2019-05-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]
