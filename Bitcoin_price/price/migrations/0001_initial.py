# Generated by Django 4.1.1 on 2022-09-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bitcoin_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
