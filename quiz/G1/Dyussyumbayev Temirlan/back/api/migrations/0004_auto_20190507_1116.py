# Generated by Django 2.2.1 on 2019-05-07 05:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20190507_1028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Contacts',
        ),
    ]