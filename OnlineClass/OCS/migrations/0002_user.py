# Generated by Django 4.2.18 on 2025-01-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('Fullname', models.CharField(max_length=100)),
            ],
        ),
    ]
