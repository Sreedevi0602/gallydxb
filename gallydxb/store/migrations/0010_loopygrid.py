# Generated by Django 5.2.3 on 2025-07-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_updatebanner2'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoopyGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/loopy/images/')),
            ],
        ),
    ]
