# Generated by Django 2.0.4 on 2018-06-14 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0005_auto_20180613_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
