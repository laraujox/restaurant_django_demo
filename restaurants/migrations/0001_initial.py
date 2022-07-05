# Generated by Django 4.0.5 on 2022-07-04 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('cep', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
                ('neighborhood', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('code', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.address')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.brand')),
            ],
            options={
                'unique_together': {('brand', 'address')},
            },
        ),
    ]