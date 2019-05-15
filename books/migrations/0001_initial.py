# Generated by Django 2.2.1 on 2019-05-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Book Title')),
                ('date_added', models.DateTimeField(verbose_name='Date Added')),
                ('location', models.CharField(max_length=100, verbose_name='Location of the book in the store')),
                ('added_by', models.CharField(max_length=60, verbose_name='Who added?')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
