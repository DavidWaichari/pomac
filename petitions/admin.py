from django.contrib import admin
from django import forms
from .models import PetitionForm, AdmissibilityForm


class PetitionFormAdminForm(forms.ModelForm):
    class Meta:
        model = PetitionForm
        fields = '__all__'


class PetitionFormAdmin(admin.ModelAdmin):
    form = PetitionFormAdminForm
    list_display = ['name', 'created', 'last_updated', 'prisonno', 'nationality', 'courtcaseno', 'ageatconviction',
                    'agewhenoffensewascommited', 'nextofkin', 'relationshipwithnextofkin', 'contactperson',
                    'telnoofcontactperson', 'location', 'nearestschool', 'homechief', 'whereoffensewascommitted',
                    'dateofconviction', 'dateofcustody', 'reliefsought', 'natureandparticularsofoffense',
                    'chargedalonefortheoffense', 'namesofcoaccused', 'knowledgeofthevictim', 'nameofvictim',
                    'areaofresidence', 'previousconvictions', 'previouspetition', 'dateofpreviouspetition',
                    'reasonofdenialofpreviouspetition', 'reasonforcurrentpetition', 'anydisplinaryactioninprison',
                    'detailsofdisplinaryactioninprison', 'anyspecialcondition', 'detailsofspecialcondition',
                    'areyouatrustee', 'dateofpromotiontotrustee', 'anyspecialattributesorskills',
                    'explanationofspecialattributesorskills', 'appealedagainsttheconviction', 'appealcaseno',
                    'appealoutcome', 'anypendingcourtmatter', 'explanationofpendingcourtmatter']
    readonly_fields = ['name', 'created', 'last_updated', 'prisonno', 'nationality', 'courtcaseno', 'ageatconviction',
                       'agewhenoffensewascommited', 'nextofkin', 'relationshipwithnextofkin', 'contactperson',
                       'telnoofcontactperson', 'location', 'nearestschool', 'homechief', 'whereoffensewascommitted',
                       'dateofconviction', 'dateofcustody', 'reliefsought', 'natureandparticularsofoffense',
                       'chargedalonefortheoffense', 'namesofcoaccused', 'knowledgeofthevictim', 'nameofvictim',
                       'areaofresidence', 'previousconvictions', 'previouspetition', 'dateofpreviouspetition',
                       'reasonofdenialofpreviouspetition', 'reasonforcurrentpetition', 'anydisplinaryactioninprison',
                       'detailsofdisplinaryactioninprison', 'anyspecialcondition', 'detailsofspecialcondition',
                       'areyouatrustee', 'dateofpromotiontotrustee', 'anyspecialattributesorskills',
                       'explanationofspecialattributesorskills', 'appealedagainsttheconviction', 'appealcaseno',
                       'appealoutcome', 'anypendingcourtmatter', 'explanationofpendingcourtmatter']


#admin.site.register(PetitionForm, PetitionFormAdmin)


class AdmissibilityFormAdminForm(forms.ModelForm):

    class Meta:
        model = AdmissibilityForm
        fields = '__all__'


class AdmissibilityFormAdmin(admin.ModelAdmin):
    form = AdmissibilityFormAdminForm
    list_display = ['created', 'last_updated', 'admissability', 'hearingdate', 'inadmissibilityreason', 'callforevidence',  'callforevidence', 'descriptionforcallofevidence', 'requestreports', 'descriptionforrequstreport', 'orderforinvestigation', 'orderforinvestigationdescription']
    readonly_fields = ['created', 'last_updated', 'admissability', 'hearingdate', 'inadmissibilityreason', 'callforevidence', 'callforevidence', 'descriptionforcallofevidence', 'requestreports', 'descriptionforrequstreport', 'orderforinvestigation', 'orderforinvestigationdescription']

#admin.site.register(AdmissibilityForm, AdmissibilityFormAdmin)
