# Generated by Django 2.2.1 on 2019-05-07 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190506_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
