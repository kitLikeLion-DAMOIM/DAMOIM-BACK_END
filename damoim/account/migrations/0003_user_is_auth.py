# Generated by Django 4.0.6 on 2022-07-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_auth',
            field=models.BooleanField(default=False),
        ),
    ]