# Generated by Django 2.2.24 on 2022-06-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20220615_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.BigIntegerField(),
        ),
    ]