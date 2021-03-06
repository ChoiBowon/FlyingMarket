# Generated by Django 2.0.5 on 2018-05-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('country_id', models.IntegerField()),
                ('created', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user_id', models.IntegerField()),
                ('is_matched', models.BooleanField(default=False)),
            ],
        ),
    ]
