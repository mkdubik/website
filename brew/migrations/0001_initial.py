# Generated by Django 2.0.4 on 2018-06-14 01:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brew_type', models.CharField(max_length=50)),
                ('yeast_addition', models.DateTimeField()),
                ('fruit', models.DecimalField(decimal_places=3, max_digits=5)),
                ('sugar', models.DecimalField(decimal_places=3, max_digits=5)),
                ('juice', models.DecimalField(decimal_places=3, max_digits=5)),
                ('preprocess', ckeditor.fields.RichTextField()),
                ('process', ckeditor.fields.RichTextField()),
                ('og', models.DecimalField(decimal_places=3, max_digits=4)),
                ('fg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('extra', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.CharField(max_length=5)),
                ('og', models.DecimalField(decimal_places=3, max_digits=4)),
                ('extra', ckeditor.fields.RichTextField()),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brew.Log')),
            ],
        ),
    ]