# Generated by Django 5.0.2 on 2024-02-26 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('is_ai_driven', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AIProblem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.skill')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.internship')),
            ],
        ),
        migrations.AddField(
            model_name='internship',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.organization'),
        ),
    ]
