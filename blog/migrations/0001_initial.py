# Generated by Django 5.2.4 on 2025-08-01 11:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogTable',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='Screenshot (3).png', null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
