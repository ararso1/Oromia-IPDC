# Generated by Django 4.2 on 2023-05-22 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IPDC', '0010_remove_domesticrequest_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='domesticrequest',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
