# Generated by Django 2.0 on 2018-05-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180507_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign',
            old_name='描述',
            new_name='description',
        ),
    ]
