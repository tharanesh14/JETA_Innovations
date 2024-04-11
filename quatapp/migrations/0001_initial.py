# Generated by Django 5.0.4 on 2024-04-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('usd', models.IntegerField(blank=True, null=True)),
                ('inr', models.IntegerField(blank=True, null=True)),
                ('result', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
