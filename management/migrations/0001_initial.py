# Generated by Django 3.2.6 on 2021-08-25 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('companyName', models.CharField(max_length=250)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('amount', models.FloatField()),
                ('paymentDue', models.DateTimeField()),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.client')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('sales', 'Sales'), ('management', 'Management'), ('support', 'Support')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField()),
                ('attendees', models.IntegerField()),
                ('eventDate', models.DateTimeField()),
                ('notes', models.TextField(max_length=2048)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.client')),
                ('eventStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.contract')),
                ('supportContact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='salesContact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee'),
        ),
        migrations.AddField(
            model_name='client',
            name='salesContact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee'),
        ),
    ]
