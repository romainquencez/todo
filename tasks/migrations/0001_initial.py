# Generated by Django 2.2.3 on 2019-07-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Nom')),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Date de création')),
                ('issue', models.PositiveIntegerField(null=True, verbose_name='Numéro de ticket')),
                ('done', models.BooleanField(default=False, verbose_name='Terminé ?')),
            ],
        ),
    ]
