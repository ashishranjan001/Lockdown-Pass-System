# Generated by Django 3.0.5 on 2020-04-04 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200405_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizenrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='corporaterequest',
            name='status',
        ),
    ]