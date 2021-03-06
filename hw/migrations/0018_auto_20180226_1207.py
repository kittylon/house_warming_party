# Generated by Django 2.0.1 on 2018-02-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0017_auto_20180223_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='invitation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hw.Invitation'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='pic',
            field=models.ImageField(default='/hw/static/images/pokeball.png', upload_to='hw/static/images'),
        ),
    ]
