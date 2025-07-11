# Generated by Django 5.2.3 on 2025-07-08 11:12

import store.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_collection1'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateBanner2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading1', models.CharField(blank=True, max_length=100, null=True)),
                ('description1', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/update_banner2/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/update_banner2/videos/', validators=[store.utils.validators.validate_video_file_extension])),
            ],
        ),
    ]
