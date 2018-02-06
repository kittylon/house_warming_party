# Generated by Django 2.0.1 on 2018-02-06 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0007_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='guest',
        ),
        migrations.AlterField(
            model_name='guest',
            name='invitation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw.Invitation'),
        ),
    ]
