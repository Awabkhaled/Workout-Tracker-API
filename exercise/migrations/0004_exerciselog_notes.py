# Generated by Django 3.2.25 on 2024-11-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20241111_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciselog',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]