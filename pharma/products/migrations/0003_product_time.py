# Generated by Django 2.2.2 on 2019-06-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190627_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
