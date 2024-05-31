# Generated by Django 4.2.13 on 2024-05-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('capacity_liquid', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('atomizer', models.CharField(max_length=100)),
                ('vape_refuel', models.CharField(max_length=100)),
                ('power', models.IntegerField()),
                ('capacity_battery', models.IntegerField()),
                ('type_battery', models.CharField(max_length=100)),
                ('type_charge', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.BinaryField()),
            ],
        ),
    ]
