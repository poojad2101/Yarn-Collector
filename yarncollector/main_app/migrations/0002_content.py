# Generated by Django 4.0.6 on 2022-07-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wool', models.CharField(max_length=100)),
                ('cotton', models.CharField(max_length=100)),
            ],
        ),
    ]
