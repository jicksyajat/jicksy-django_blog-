# Generated by Django 5.1.2 on 2024-10-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='todo title')),
                ('content', models.TextField(max_length=30, verbose_name='descrption')),
                ('pdate', models.DateField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
