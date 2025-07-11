# Generated by Django 5.2.3 on 2025-07-07 12:22

import store.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/categories/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/categories/videos/', validators=[store.utils.validators.validate_video_file_extension])),
            ],
        ),
    ]
