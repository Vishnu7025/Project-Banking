# Generated by Django 4.1.2 on 2022-10-21 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
