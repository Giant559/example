# Generated by Django 3.0.3 on 2020-03-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='Null', max_length=200),
        ),
    ]
