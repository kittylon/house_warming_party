# Generated by Django 2.0.1 on 2018-02-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0010_auto_20180206_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
