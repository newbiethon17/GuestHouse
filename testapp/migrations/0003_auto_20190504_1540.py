# Generated by Django 2.1.7 on 2019-05-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_post_concert_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_period',
            new_name='concert_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_time',
            new_name='post_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.AddField(
            model_name='post',
            name='owner_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='singer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
