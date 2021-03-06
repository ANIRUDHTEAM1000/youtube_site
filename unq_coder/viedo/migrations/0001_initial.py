# Generated by Django 3.1.2 on 2020-10-20 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('playname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='D:\\DjangoProjects\\unq_coder\\media')),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Viedo',
            fields=[
                ('Vname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
                ('iframelink', models.CharField(max_length=100)),
                ('vedioNumber', models.ImageField(upload_to='')),
                ('istop', models.BooleanField(default=False)),
                ('tags', models.CharField(max_length=100)),
                ('playname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viedo.playlist')),
            ],
        ),
    ]
