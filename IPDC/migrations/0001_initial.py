# Generated by Django 4.1.3 on 2023-03-10 06:49

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
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('middle_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phonenumber', models.CharField(max_length=300)),
                ('education_level', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('current_Address', models.CharField(max_length=300)),
                ('Tin', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
