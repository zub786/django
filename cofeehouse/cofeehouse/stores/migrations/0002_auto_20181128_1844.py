# Generated by Django 2.2 on 2018-11-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
