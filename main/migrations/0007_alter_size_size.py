# Generated by Django 5.1.5 on 2025-02-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_name_brand_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('UK 6', 'UK 6'), ('UK 7', 'UK 7'), ('UK 8', 'UK 8'), ('UK 9', 'UK 9')], max_length=10, verbose_name='Размер'),
        ),
    ]
