# Generated by Django 3.0.5 on 2020-06-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='profile_pic',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]