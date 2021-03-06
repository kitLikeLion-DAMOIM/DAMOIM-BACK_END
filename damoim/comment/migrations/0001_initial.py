# Generated by Django 4.0.4 on 2022-07-10 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(help_text='Comment ID', primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=10)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(db_column='post_id', default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='post.post')),
            ],
        ),
    ]
