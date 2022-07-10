# Generated by Django 4.0.6 on 2022-07-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_id',
            field=models.ForeignKey(db_column='group_id', default='', on_delete=django.db.models.deletion.CASCADE, related_name='group', to='group.group'),
        ),
    ]