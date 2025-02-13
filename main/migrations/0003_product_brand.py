from django.db import migrations


def clear_product_brands(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    Product.objects.update(brand=None)  # Устанавливаем значение brand в NULL


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_alter_category_options_category_parent'),  # Укажите правильное имя предыдущей миграции
    ]

    operations = [
        migrations.RunPython(clear_product_brands),
    ]
