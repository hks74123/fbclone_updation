# Generated by Django 3.2.5 on 2022-02-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hksfbclone', '0007_alter_group_request_from_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_groups',
            name='groupcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
