# Generated by Django 2.0.7 on 2019-05-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '1005_auto_20190214_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petitionform',
            options={'ordering': ('-created',), 'permissions': (('can_view_petitionforms', 'User can view all petitions'), ('can_view_mypetitionforms', 'User can view all my petitions'), ('can_view_petitionformstatus', 'User can view the status of petitions'), ('can_view_duplicatesfinder', 'User can view the petitions duplicates'), ('can_view_petitionformdetails', 'User can view the details of petitions'), ('can_view_main_dashboard', 'User can view main dashboard'), ('can_view_more_reports', 'User can view more reports dashboard'), ('can_modifydates_created', 'User can modify dates of creation/submission'))},
        ),
        migrations.AlterField(
            model_name='petitionsummary',
            name='admissibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitions.AdmissibilityForm'),
        ),
    ]
