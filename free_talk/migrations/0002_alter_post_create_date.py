# Generated by Django 4.0.4 on 2022-05-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
