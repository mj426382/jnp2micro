# Generated by Django 3.1.7 on 2021-07-25 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_group_task_optional_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group_task',
        ),
    ]
