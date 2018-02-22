# Generated by Django 2.0.1 on 2018-02-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0012_gift_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='status',
            field=models.CharField(choices=[('Going', 'Y'), ('Not going', 'N')], max_length=11),
        ),
        migrations.AlterField(
            model_name='gift',
            name='pic',
            field=models.ImageField(default='/hw/static/images/pokeball.png', upload_to='hw/static/images'),
        ),
    ]