# Generated by Django 2.2.4 on 2019-12-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='shopkeeper_name',
            field=models.CharField(default='', max_length=90),
        ),
    ]