# Generated by Django 3.0.4 on 2020-03-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mastered_list',
            field=models.TextField(default=''),
        ),
    ]
