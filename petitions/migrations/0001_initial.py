# Generated by Django 2.1 on 2018-08-23 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissibilityForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('admissability', models.BooleanField()),
                ('hearingdate', models.DateField(blank=True, null=True)),
                ('inadmissibilityreason', models.TextField(blank=True, max_length=300, null=True)),
                ('callforevidence', models.BooleanField()),
                ('descriptionforcallofevidence', models.TextField(blank=True, max_length=300, null=True)),
                ('requestreports', models.BooleanField()),
                ('descriptionforrequstreport', models.TextField(blank=True, max_length=300, null=True)),
                ('orderforinvestigation', models.BooleanField()),
                ('orderforinvestigationdescription', models.TextField(blank=True, max_length=300, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='HearingSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('healthstatus', models.TextField(max_length=400)),
                ('familystatus', models.TextField(max_length=400)),
                ('natureandseriousnessoftheoffense', models.TextField(max_length=400)),
                ('personalcircumstances', models.TextField(max_length=400)),
                ('interestofstateandcommunity', models.TextField(max_length=400)),
                ('postconvictionconduct', models.TextField(max_length=400)),
                ('officialrecommendationsandreports', models.TextField(max_length=400)),
                ('wherethepetitionerhaspersued', models.TextField(max_length=400)),
                ('representationofvictim', models.TextField(max_length=400)),
                ('reportoffellowinmates', models.TextField(max_length=400)),
                ('reportsfromprobationservices', models.TextField(max_length=1000)),
                ('observationswithmainreasons', models.TextField(max_length=1000)),
                ('action', models.CharField(max_length=100)),
                ('interviewdate', models.DateField(blank=True, null=True)),
                ('reviewdate', models.DateField(blank=True, null=True)),
                ('actiondescription', models.TextField(max_length=400)),
                ('member1', models.CharField(max_length=100)),
                ('member2', models.CharField(max_length=100)),
                ('member3', models.CharField(max_length=100)),
                ('member4', models.CharField(max_length=100)),
                ('member5', models.CharField(max_length=100)),
                ('member6', models.CharField(max_length=100)),
                ('member7', models.CharField(max_length=100)),
                ('member8', models.CharField(max_length=100)),
                ('member9', models.CharField(max_length=100)),
                ('member10', models.CharField(max_length=100)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('admissibility', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hearing', to='petitions.AdmissibilityForm')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='InterviewSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('ownaccountofcircumstances', models.TextField(max_length=1000)),
                ('reconciliationefforts', models.TextField(max_length=1000)),
                ('indicationofremosefulness', models.TextField(max_length=1000)),
                ('anyothercomments', models.TextField(max_length=1000)),
                ('representationofthevictim', models.TextField(max_length=100)),
                ('concludingobservations', models.TextField(max_length=1000)),
                ('chairpersonvote', models.BooleanField()),
                ('chairpersonvotereason', models.TextField(max_length=300)),
                ('vicechairvote', models.BooleanField()),
                ('vicechairvotereason', models.TextField(max_length=100)),
                ('csvote', models.NullBooleanField()),
                ('csvotereason', models.TextField(max_length=100)),
                ('m1vote', models.NullBooleanField()),
                ('m1votereason', models.TextField(max_length=100)),
                ('m2vote', models.NullBooleanField()),
                ('m2votereason', models.TextField(max_length=100)),
                ('m3vote', models.NullBooleanField()),
                ('m3votereason', models.TextField(max_length=100)),
                ('m4vote', models.NullBooleanField()),
                ('m4votereason', models.TextField(max_length=100)),
                ('m5vote', models.NullBooleanField()),
                ('m5votereason', models.TextField(max_length=100)),
                ('m6vote', models.NullBooleanField()),
                ('m6votereason', models.TextField(max_length=100)),
                ('finalresolution', models.CharField(max_length=30)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hearing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='petitions.HearingSummary')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PetitionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=30)),
                ('prison', models.CharField(max_length=50)),
                ('prisonno', models.CharField(max_length=30, unique=True)),
                ('court', models.CharField(max_length=50)),
                ('courtcaseno', models.CharField(max_length=30)),
                ('dateofconviction', models.DateField()),
                ('dateofcustody', models.DateField()),
                ('ageatconviction', models.IntegerField()),
                ('agewhenoffensewascommited', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('nextofkin', models.CharField(max_length=50)),
                ('relationshipwithnextofkin', models.CharField(max_length=50)),
                ('contactperson', models.CharField(max_length=50)),
                ('telnoofcontactperson', models.CharField(max_length=15)),
                ('nearestschool', models.CharField(max_length=50)),
                ('homechief', models.CharField(max_length=30)),
                ('whereoffensewascommitted', models.CharField(max_length=50)),
                ('convictedforlife', models.BooleanField()),
                ('sentence', models.IntegerField(blank=True, null=True)),
                ('reliefsought', models.CharField(max_length=100)),
                ('offence', models.CharField(max_length=100)),
                ('natureandparticularsofoffense', models.TextField(max_length=500)),
                ('chargedalonefortheoffense', models.BooleanField()),
                ('namesofcoaccused', models.TextField(max_length=100)),
                ('knowledgeofthevictim', models.BooleanField()),
                ('nameofvictim', models.CharField(max_length=30)),
                ('areaofresidence', models.CharField(max_length=30)),
                ('previousconvictions', models.TextField(max_length=300)),
                ('previouspetition', models.BooleanField()),
                ('dateofpreviouspetition', models.DateField(null=True)),
                ('reasonofdenialofpreviouspetition', models.TextField(max_length=100)),
                ('reasonforcurrentpetition', models.TextField(max_length=300)),
                ('anydisplinaryactioninprison', models.BooleanField()),
                ('detailsofdisplinaryactioninprison', models.TextField(max_length=300)),
                ('anyspecialcondition', models.BooleanField()),
                ('detailsofspecialcondition', models.TextField(max_length=100)),
                ('areyouatrustee', models.BooleanField()),
                ('dateofpromotiontotrustee', models.DateField(null=True)),
                ('anyspecialattributesorskills', models.BooleanField()),
                ('explanationofspecialattributesorskills', models.TextField(max_length=300)),
                ('appealedagainsttheconviction', models.BooleanField()),
                ('appealcaseno', models.CharField(max_length=30)),
                ('appealoutcome', models.TextField(max_length=100)),
                ('anypendingcourtmatter', models.BooleanField()),
                ('explanationofpendingcourtmatter', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitions.County')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PetitionSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeandcircumstancesofoffence', models.TextField(max_length=1000)),
                ('petitionoverview', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('admissibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitions.AdmissibilityForm')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='RecommendationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('explanationofrecommedation', models.TextField(max_length=1000)),
                ('mercy', models.CharField(max_length=200)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('interview', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='petitions.InterviewSummary')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitions.County')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='petitionform',
            name='subcounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitions.SubCounty'),
        ),
        migrations.AddField(
            model_name='admissibilityform',
            name='petitioner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admissibility', to='petitions.PetitionForm'),
        ),
    ]
