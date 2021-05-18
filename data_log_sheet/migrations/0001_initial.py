# Generated by Django 3.2.3 on 2021-05-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLogSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reel', models.CharField(max_length=200)),
                ('epi', models.IntegerField()),
                ('scn', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('clips', models.CharField(max_length=200)),
                ('shot', models.IntegerField()),
                ('take', models.IntegerField()),
                ('note', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('epi',),
            },
        ),
    ]
