# Generated by Django 4.0.3 on 2022-05-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirius_api', '0011_alter_alat_gambar_alat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alat',
            name='gambar_alat',
            field=models.ImageField(upload_to='gambar_alat/'),
        ),
    ]
