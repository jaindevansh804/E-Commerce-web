# Generated by Django 3.2.5 on 2021-10-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]