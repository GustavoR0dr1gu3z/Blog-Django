# Generated by Django 4.2.11 on 2024-05-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='order',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
