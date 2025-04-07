# Generated by Django 5.1.6 on 2025-04-06 23:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('conge', 'Congé'), ('maladie', 'Maladie'), ('autre', 'Autre')], max_length=20)),
                ('description', models.TextField()),
                ('statut', models.CharField(default='en_attente', max_length=20)),
                ('vu', models.BooleanField(default=False)),
                ('manager_reponse', models.TextField(blank=True, null=True)),
                ('date_reponse', models.DateTimeField(blank=True, null=True)),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
