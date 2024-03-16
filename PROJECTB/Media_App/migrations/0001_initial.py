# Generated by Django 4.1.4 on 2023-01-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Households',
            fields=[
                ('hid', models.IntegerField(db_column='hID', primary_key=True, serialize=False)),
                ('networth', models.IntegerField(blank=True, db_column='netWorth', null=True)),
                ('childrenNum', models.IntegerField(blank=True, db_column='ChildrenNum', null=True)),
            ],
            options={
                'db_table': 'Households',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('title', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('genre', models.CharField(blank=True, max_length=25, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Programs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramRanks',
            fields=[
                ('title', models.OneToOneField(db_column='title', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Media_App.programs')),
                ('rank', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ProgramRanks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecordOrders',
            fields=[
                ('title', models.OneToOneField(db_column='title', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Media_App.programs')),
            ],
            options={
                'db_table': 'RecordOrders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecordReturns',
            fields=[
                ('title', models.OneToOneField(db_column='title', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Media_App.programs')),
            ],
            options={
                'db_table': 'RecordReturns',
                'managed': False,
            },
        ),
    ]
