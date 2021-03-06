# Generated by Django 3.1.4 on 2020-12-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screening', '0006_auto_20201223_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hasscreened',
            name='screening_date_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hasscreened',
            name='region',
            field=models.CharField(choices=[('East', 'East'), ('Extreme_North', 'Extreme_North'), ('Adamaoua', 'Adamaoua'), ('North_West', 'North_West'), ('West', 'West'), ('South', 'South'), ('Centre', 'Centre'), ('Littoral', 'Littoral'), ('North', 'North'), ('South_West', 'South_West')], max_length=13),
        ),
        migrations.AlterField(
            model_name='hasscreened',
            name='status',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('?', '?'), ('r', 'r'), ('d', 'd')], max_length=1),
        ),
    ]
