# Generated by Django 4.2 on 2023-05-26 07:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPDC', '0012_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytext', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]