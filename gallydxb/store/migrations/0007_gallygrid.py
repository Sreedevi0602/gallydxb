# Generated by Django 5.2.3 on 2025-07-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_productmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='GallyGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/gally/images/')),
            ],
        ),
    ]
