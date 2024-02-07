# Generated by Django 4.2.5 on 2023-11-10 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sadeem_backend', '0019_imgurtoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgurtoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
