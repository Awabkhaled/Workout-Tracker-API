# Generated by Django 3.2.25 on 2024-11-13 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0008_auto_20241113_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciselog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
