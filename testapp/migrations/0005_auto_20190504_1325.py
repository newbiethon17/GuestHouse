# Generated by Django 2.1.8 on 2019-05-04 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20190504_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=1000)),
                ('number', models.CharField(default='', max_length=1000)),
                ('pwd', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='pwd',
            new_name='owner_pwd',
        ),
        migrations.AlterField(
            model_name='post',
            name='owner_number',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='member',
            name='chosen_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Post'),
        ),
    ]
