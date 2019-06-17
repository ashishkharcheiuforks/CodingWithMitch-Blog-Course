# Generated by Django 2.2.2 on 2019-06-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('question', models.TextField(max_length=400)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
            ],
            options={
                'verbose_name': 'The Question',
                'verbose_name_plural': 'Questions from People',
            },
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]