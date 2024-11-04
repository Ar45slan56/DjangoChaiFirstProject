# Generated by Django 5.1.2 on 2024-10-13 20:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVriety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('EL', 'Elachi'), ('CD', 'Cold'), ('ML', 'Masala')], max_length=2)),
            ],
        ),
    ]
