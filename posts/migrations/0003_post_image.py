# Generated by Django 4.1.6 on 2023-10-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_titele_post_title_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='\\Post'),
            preserve_default=False,
        ),
    ]
