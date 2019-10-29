# Generated by Django 2.2.1 on 2019-10-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowndb', '0004_auto_20191016_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusId', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusId', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]
