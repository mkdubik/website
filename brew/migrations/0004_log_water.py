# Generated by Django 2.0.4 on 2018-06-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0003_auto_20180614_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='water',
            field=models.DecimalField(decimal_places=3, default=3, max_digits=5),
            preserve_default=False,
        ),
    ]