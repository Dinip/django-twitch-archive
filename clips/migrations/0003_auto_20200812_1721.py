# Generated by Django 3.1 on 2020-08-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0002_auto_20200812_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='video_id',
            field=models.IntegerField(null=True),
        ),
    ]
