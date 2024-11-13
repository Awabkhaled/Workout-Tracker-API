# Generated by Django 3.2.25 on 2024-11-13 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_exerciselog_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciselog',
            name='created_at',
        ),
        migrations.AddField(
            model_name='exercise',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
