# Generated by Django 4.1.1 on 2022-09-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]