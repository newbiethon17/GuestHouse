# Generated by Django 2.1.8 on 2019-05-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20190504_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='now_capacity',
            field=models.IntegerField(default=0),
        ),
    ]
