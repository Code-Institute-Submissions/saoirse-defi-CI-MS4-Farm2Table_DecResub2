# Generated by Django 3.2.7 on 2021-09-30 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_alter_product_seller_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller_id',
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
