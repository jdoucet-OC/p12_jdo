# Generated by Django 3.2.6 on 2021-09-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_client_dateupdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dateUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dateUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='dateUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
