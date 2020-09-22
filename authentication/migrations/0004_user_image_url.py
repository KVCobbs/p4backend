# Generated by Django 3.1.1 on 2020-09-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.URLField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
