# Generated by Django 3.0.2 on 2020-01-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=10)),
                ('colour', models.CharField(max_length=20)),
            ],
        ),
    ]
