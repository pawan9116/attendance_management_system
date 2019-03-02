# Generated by Django 2.1.7 on 2019-03-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eigth')], default=0)),
            ],
        ),
    ]
