# Generated by Django 5.0.6 on 2024-06-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]
