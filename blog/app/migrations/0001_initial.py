# Generated by Django 4.1.1 on 2022-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('url', models.URLField(blank=True)),
                ('content', models.CharField(max_length=100000)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
