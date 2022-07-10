# Generated by Django 4.0.4 on 2022-07-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_category', models.CharField(max_length=50, null=True)),
                ('logo', models.TextField()),
                ('group_name', models.CharField(max_length=50)),
                ('profile_link', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('detail', models.TextField()),
            ],
        ),
    ]
