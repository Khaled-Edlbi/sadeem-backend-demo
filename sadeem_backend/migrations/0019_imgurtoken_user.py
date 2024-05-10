# Generated by Django 4.2.5 on 2023-11-10 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sadeem_backend', '0018_imgurtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgurtoken',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]