# Generated by Django 2.1.4 on 2018-12-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]