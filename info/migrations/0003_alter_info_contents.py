# Generated by Django 3.2 on 2022-08-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_info_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='contents',
            field=models.CharField(max_length=5000),
        ),
    ]
