# Generated by Django 5.0.7 on 2024-09-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
