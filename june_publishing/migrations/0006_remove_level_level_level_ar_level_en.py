# Generated by Django 4.2.5 on 2024-06-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('june_publishing', '0005_remove_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='level',
        ),
        migrations.AddField(
            model_name='level',
            name='ar',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='en',
            field=models.CharField(max_length=10, null=True),
        ),
    ]