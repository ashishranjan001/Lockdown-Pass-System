# Generated by Django 3.0.5 on 2020-04-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.IntegerField()),
                ('req_date', models.DateField()),
                ('req_time', models.TimeField()),
                ('req_duration', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CorporateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.IntegerField()),
                ('organization_name', models.CharField(max_length=50)),
                ('cin_no', models.CharField(max_length=30)),
                ('industry_type', models.CharField(max_length=30)),
                ('num_requested', models.IntegerField()),
                ('req_date', models.DateField()),
                ('req_time', models.TimeField()),
                ('req_duration', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('aadhaar', models.IntegerField(primary_key=True, serialize=False)),
                ('usertype', models.CharField(max_length=10)),
            ],
        ),
    ]
