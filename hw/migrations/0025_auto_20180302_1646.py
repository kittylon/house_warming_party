# Generated by Django 2.0.1 on 2018-03-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0024_gift_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='inv_type',
            field=models.CharField(choices=[('Giver', 'G'), ('Single', 'S'), ('Couple', 'C')], max_length=10),
        ),
    ]