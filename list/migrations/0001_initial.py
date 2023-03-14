# Generated by Django 3.2 on 2022-08-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=50)),
                ('contents', models.CharField(max_length=5000)),
                ('thema', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=5, max_digits=11)),
                ('lon', models.DecimalField(decimal_places=5, max_digits=11)),
            ],
        ),
    ]