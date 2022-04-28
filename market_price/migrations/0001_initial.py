# Generated by Django 4.0.4 on 2022-04-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkPriceInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('lineup', models.CharField(blank=True, max_length=50)),
                ('aged', models.PositiveIntegerField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('purchasing_route', models.CharField(max_length=100)),
                ('purchasing_date', models.DateField()),
                ('recoding_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]