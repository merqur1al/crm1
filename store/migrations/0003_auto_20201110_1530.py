# Generated by Django 3.0.7 on 2020-11-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
