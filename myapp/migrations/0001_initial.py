# Generated by Django 2.2.7 on 2020-01-13 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True)),
                ('top_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Topic')),
            ],
        ),
    ]
