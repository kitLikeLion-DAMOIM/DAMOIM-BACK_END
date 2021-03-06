# Generated by Django 4.0.4 on 2022-07-10 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(db_column='group_id', default='', on_delete=django.db.models.deletion.CASCADE, related_name='group', to='group.group')),
            ],
        ),
    ]
