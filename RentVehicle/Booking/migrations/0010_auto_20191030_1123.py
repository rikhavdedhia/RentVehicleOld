# Generated by Django 2.2.1 on 2019-10-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_auto_20191030_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='negotiationPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]