# Generated by Django 2.2.2 on 2019-07-03 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_s_totla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='s_totla',
            new_name='s_total',
        ),
    ]
