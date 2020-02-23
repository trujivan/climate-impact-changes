# Generated by Django 3.0.3 on 2020-02-23 00:33

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(default=2017)),
                ('end_year', models.IntegerField(default=2020)),
                ('state', models.CharField(max_length=100)),
                ('factor', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='yearmodel',
            name='year',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)], default=api.models.current_year),
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('pollution', models.DecimalField(decimal_places=2, max_digits=32)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='api.MLRequest')),
            ],
        ),
    ]
