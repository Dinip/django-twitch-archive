# Generated by Django 3.1 on 2020-08-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0018_auto_20200815_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='on_twitch',
            field=models.BooleanField(default=False),
        ),
    ]
