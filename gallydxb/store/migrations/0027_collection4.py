# Generated by Django 5.2.3 on 2025-07-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_districtgrid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='uploads/collection4/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/collection4/')),
            ],
        ),
    ]
