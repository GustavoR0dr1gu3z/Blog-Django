# Generated by Django 4.2.11 on 2024-05-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
