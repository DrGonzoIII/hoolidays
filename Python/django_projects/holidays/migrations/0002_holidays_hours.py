# Generated by Django 2.1.2 on 2018-10-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidays',
            name='hours',
            field=models.IntegerField(default=8),
        ),
    ]
