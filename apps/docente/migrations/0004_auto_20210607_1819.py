# Generated by Django 3.1.6 on 2021-06-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0003_auto_20210607_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='codigo',
        ),
        migrations.AddField(
            model_name='docente',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
