# Generated by Django 4.0.4 on 2022-04-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_price', '0006_rename_recoding_date_drinkpriceinformation_recoded_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkpriceinformation',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
