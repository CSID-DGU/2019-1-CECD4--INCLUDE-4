# Generated by Django 2.2.4 on 2019-11-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20191124_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttoken',
            name='requestcode',
            field=models.IntegerField(default=0),
        ),
    ]