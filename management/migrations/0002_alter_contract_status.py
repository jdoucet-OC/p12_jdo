# Generated by Django 3.2.6 on 2021-08-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]