# Generated by Django 4.2.3 on 2023-11-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_food_foodbooking_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_id', models.IntegerField()),
                ('Amount', models.CharField(max_length=30)),
                ('User_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Table_id', models.IntegerField()),
                ('Table_name', models.CharField(max_length=50)),
                ('Time', models.TimeField()),
                ('Amount', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tableBooking',
            },
        ),
    ]
