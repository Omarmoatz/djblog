# Generated by Django 4.1.6 on 2023-10-05 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titele',
            new_name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]