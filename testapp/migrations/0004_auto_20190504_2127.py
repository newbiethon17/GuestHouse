# Generated by Django 2.1.7 on 2019-05-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20190504_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='owner_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='pwd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='concert_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='concert_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner_email',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='singer',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
