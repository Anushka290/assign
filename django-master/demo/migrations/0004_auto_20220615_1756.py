# Generated by Django 2.2.24 on 2022-06-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20220615_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(max_length=13),
        ),
    ]
