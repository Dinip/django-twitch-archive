# Generated by Django 3.1 on 2020-08-14 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0016_auto_20200814_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitchsettings',
            name='created_at',
        ),
    ]
