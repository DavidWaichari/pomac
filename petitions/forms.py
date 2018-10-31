from django import forms
from .models import PetitionForm, AdmissibilityForm, HearingSummary, InterviewSummary, RecommendationForm, \
    PetitionSummary, SubCounty, County, Exit, Prison, Court, Offence, Grant


class CountyForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name']

class SubCountyForm(forms.ModelForm):
    class Meta:
        model = SubCounty
        fields = ['name', 'county']

class PrisonForm(forms.ModelForm):
    class Meta:
        model = Prison
        fields = ['name']


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['name']


class OffenceForm(forms.ModelForm):
    class Meta:
        model = Offence
        fields = ['name']


class PetitionFormForm(forms.ModelForm):
    def boolean_coerce(value):
        # value is received as a unicode string
        if str(value).lower() in ('1', 'true'):
            return True
        elif str(value).lower() in ('0', 'false'):
            return False

    reliefsoughtcategories = [
        ('', 'Select as appropriate'),
        ('Free or conditional pardon', 'Free or conditional pardon'),
        ('Postponing the carrying out of a punishment for a specific or indefinite period ',
         'Postponing the carrying out of a punishment for a specific or indefinite period '),
        ('Subsituting a less severe form of punishment', 'Subsituting a less severe form of punishment'),
        ('Remitting all or part of punishment', 'Remitting all or part of punishment')
    ]

    name = forms.CharField(label='Name of convicted criminal offender',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    selectnationality = forms.TypedChoiceField(label='Select Nationality',
                                               coerce=boolean_coerce,
                                               choices=((True, 'Kenyan'), (False, 'Foreigner')),
                                               widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}))
    nationality = forms.CharField(label='Nationality', widget=forms.TextInput(attrs={'class': 'form-control','value':'Kenyan'}))
    prison = forms.ModelChoiceField(queryset=Prison.objects.order_by('name'), label='Prison where held', widget=forms.Select(attrs={'class':'form-control'}))
    prisonno = forms.CharField(label='Prison Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    court = forms.ModelChoiceField(queryset=Court.objects.order_by('name'), label='Court Where Convicted', widget=forms.Select(attrs={'class':'form-control'}))
    courtcaseno = forms.CharField(label='Court case number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateofconviction = forms.DateField(label='Date of conviction', widget=forms.DateInput(format=('%m/%d/%Y'), attrs={
        'class': 'form-control datepicker'}))
    dateofcustody = forms.DateField(label='Date of custody (remand)', widget=forms.DateInput(format=('%m/%d/%Y'),
                                                                                             attrs={
                                                                                                 'class': 'datepicker form-control'}))
    ageatconviction = forms.IntegerField(label='Age at conviction',
                                         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    agewhenoffensewascommited = forms.IntegerField(label='Age when the offence was committed',
                                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))
    county = forms.ModelChoiceField(queryset=County.objects.order_by('name'), label='Home County', widget=forms.Select(attrs={'class':'form-control'}))
    subcounty = forms.ModelChoiceField(queryset=SubCounty.objects.order_by('name'), label='Sub County', widget=forms.Select(attrs={'class':'form-control'}))
    location = forms.CharField(label='Home Location', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nextofkin = forms.CharField(label='Next of kin', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    relationshipwithnextofkin = forms.CharField(label='Relationship with the next of kin', required=False,
                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    contactperson = forms.CharField(label='Contact person', required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    telnoofcontactperson = forms.CharField(label='Tel No. of the contact person', required=False,
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    nearestschool = forms.CharField(label='Nearest school', widget=forms.TextInput(attrs={'class': 'form-control'}))
    homechief = forms.CharField(label='Name of Home the Chief', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    whereoffensewascommitted = forms.CharField(label='Where the offense was committed',
                                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    convictedforlife = forms.TypedChoiceField(label='Were you sentenced to life imprisonment / death/ Presidential Pleasure',
                                              coerce=boolean_coerce,
                                              choices=((True, 'Yes'), (False, 'No')),
                                              widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}))
    sentence = forms.IntegerField(required=False,
                               label='If No, the number of years sentenced',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reliefsought = forms.CharField(label='Relief sought or nature of the petition',
                                   widget=forms.Select(choices=reliefsoughtcategories,
                                                       attrs={'class': 'form-control'}))
    offence = forms.ModelChoiceField(queryset=Offence.objects.order_by('name'), label='Offence', widget=forms.Select(attrs={'class':'form-control'}))
    natureandparticularsofoffense = forms.CharField(
        label='The nature, particulars and circumstances surrounding the commission of the offense ',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    chargedalonefortheoffense = forms.TypedChoiceField(label='Were you charged alone for the offense?',
                                                       coerce=boolean_coerce,
                                                       choices=((True, 'Yes'), (False, 'No')),
                                                       widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}))
    namesofcoaccused = forms.CharField(required=False,
                                       label='If No, give the names of the co-accused and prison held if they were convicted',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    knowledgeofthevictim = forms.TypedChoiceField(
        label='Do you know the victim of the offense for which you were charged?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}))
    nameofvictim = forms.CharField(label='if Yes, indicate the Name of the victim', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    areaofresidence = forms.CharField(label='and the Area of residence (if known)', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    previousconvictions = forms.CharField(label='State and explain any previous conviction(s) where applicable',
                                          required=False,
                                          widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    previouspetition = forms.TypedChoiceField(label='Has the petitioner made any previous petition?',
                                              coerce=boolean_coerce,
                                              choices=((True, 'Yes'), (False, 'No')),
                                              widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    dateofpreviouspetition = forms.DateField(required=False, label='If yes, Date of the previous petition was',
                                             widget=forms.DateInput(format=('%m/%d/%Y'),
                                                                    attrs={'class': 'datepicker form-control'}))
    reasonofdenialofpreviouspetition = forms.CharField(label='And the reason of denial of previous petition',
                                                       required=False,
                                                       widget=forms.Textarea(
                                                           attrs={'class': 'form-control', 'rows': 4}))
    reasonforcurrentpetition = forms.CharField(label='Reasons for current petitioning',
                                               widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    anydisplinaryactioninprison = forms.TypedChoiceField(
        label='Have you had any disciplinary action taken against you while in prison?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    detailsofdisplinaryactioninprison = forms.CharField(label='If yes give the details of the disciplinary action',
                                                        required=False, widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 4}))
    anyspecialcondition = forms.TypedChoiceField(
        label='Any special condition e.g physical ability challenges, terminal sickness, very sickly, '
              'mental health etc?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    detailsofspecialcondition = forms.CharField(label='If yes, give the details of special condition', required=False,
                                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    areyouatrustee = forms.TypedChoiceField(label='Are you a trustee?',
                                            coerce=boolean_coerce,
                                            choices=((True, 'Yes'), (False, 'No')),
                                            widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    dateofpromotiontotrustee = forms.DateField(required=False, label='If yes, when were you promoted to trustee',
                                               widget=forms.DateInput(format=('%m/%d/%Y'),
                                                                      attrs={'class': 'datepicker form-control'}))
    anyspecialattributesorskills = forms.TypedChoiceField(
        label='Are you recognized for special attributes, achievements or skills attained in prison?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    explanationofspecialattributesorskills = forms.CharField(label='If yes, please explain', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 4}), required=False)
    appealedagainsttheconviction = forms.TypedChoiceField(label='Did you appeal against the conviction?',
                                                          coerce=boolean_coerce,
                                                          choices=((True, 'Yes'), (False, 'No')),
                                                          widget=forms.RadioSelect(
                                                              attrs={'style': 'margin-left: 30px;'}), )
    appealcaseno = forms.CharField(label='If yes, indicate the Appeal Case Numbers',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), required=False)
    appealoutcome = forms.CharField(label='and, the Outome of the Appeal',
                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), required=False)
    anypendingcourtmatter = forms.TypedChoiceField(
        label='Do you have any pending court matter even if not related to your conviction?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    explanationofpendingcourtmatter = forms.CharField(required=False, label='if yes, please explain',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    isttheapplicantthepetitioner = forms.TypedChoiceField(
        label='Is the applicant of this petition the petitioner?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    nameofapplicant = forms.CharField(label='If No, the name of the applicant is', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))

    relationshipofapplicantwithpetitioner = forms.CharField(label='And the relationship to the petitioner', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    addressoftheapplicant = forms.CharField(label='And the Postal Adress of the applicant', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephonenumberoftheapplicant = forms.CharField(label='And the telephone number of the applicant', required=False,
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcounty'].queryset = SubCounty.objects.none()

        if 'county' in self.data:
            try:
                county_id = int(self.data.get('county'))
                self.fields['subcounty'].queryset = SubCounty.objects.filter(county_id=county_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty SubCounty queryset
        elif self.instance.pk:
            self.fields['subcounty'].queryset = self.instance.county.subcounty_set.order_by('name')

    class Meta:
        model = PetitionForm
        fields = ['name','selectnationality','nationality', 'prison', 'prisonno', 'court', 'courtcaseno',
                  'dateofcustody','dateofconviction',
                  'ageatconviction', 'agewhenoffensewascommited', 'county', 'subcounty', 'location',
                  'nextofkin', 'relationshipwithnextofkin',
                  'contactperson', 'telnoofcontactperson', 'nearestschool', 'homechief', 'convictedforlife', 'sentence',
                  'whereoffensewascommitted', 'reliefsought','offence',
                  'natureandparticularsofoffense', 'chargedalonefortheoffense', 'namesofcoaccused',
                  'knowledgeofthevictim', 'nameofvictim', 'areaofresidence', 'previousconvictions',
                  'previouspetition', 'dateofpreviouspetition', 'reasonofdenialofpreviouspetition',
                  'reasonforcurrentpetition', 'anydisplinaryactioninprison', 'detailsofdisplinaryactioninprison',
                  'anyspecialcondition', 'detailsofspecialcondition', 'areyouatrustee', 'dateofpromotiontotrustee',
                  'anyspecialattributesorskills', 'explanationofspecialattributesorskills',
                  'appealedagainsttheconviction', 'appealcaseno', 'appealoutcome', 'anypendingcourtmatter',
                  'explanationofpendingcourtmatter','isttheapplicantthepetitioner','nameofapplicant','relationshipofapplicantwithpetitioner','addressoftheapplicant','telephonenumberoftheapplicant']



class AdmissibilityCreateForm(forms.ModelForm):
    def boolean_coerce(value):
        # value is received as a unicode string
        if str(value).lower() in ('1', 'true'):
            return True
        elif str(value).lower() in ('0', 'false'):
            return False

    petitioner = forms.ModelChoiceField(label='Choose Petitioner',queryset=PetitionForm.objects.filter(anypendingcourtmatter=False).filter(admissibilityform__isnull=True).filter(exit__isnull=True), widget=forms.Select(attrs={'class': 'form-control'}))

    admissability = forms.TypedChoiceField(
        label='Do you wish to render the this petition ADMISSIBLE?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    hearingdate = forms.DateField(required=False, label='If yes, Hear the petition taking into account the criteria provided in Section 22 of the '
                                                        'Power of Mercy Act, 2011 on the following date',
                                               widget=forms.DateInput(format=('%m/%d/%Y'),
                                                                      attrs={'class': 'datepicker form-control'}))
    inadmissibilityreason = forms.CharField(required=False, label='If no, give a reason why it is  INADMISSIBLE',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    callforevidence = forms.TypedChoiceField(
        label='Do you wish to call for more evidence?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    descriptionforcallofevidence =  forms.CharField(required=False, label='if yes, please explain',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    requestreports =  forms.TypedChoiceField(
        label='Do you wish to Request reports from various Goverrment Agencies?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    descriptionforrequstreport = forms.CharField(required=False, label='if yes, please list the Government Agencies',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    orderforinvestigation = forms.TypedChoiceField(
        label='Do you wish to order for more investigations?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    orderforinvestigationdescription = forms.CharField(required=False, label='if yes, please explain',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = AdmissibilityForm
        fields = [ 'petitioner','admissability', 'hearingdate', 'inadmissibilityreason', 'callforevidence', 'descriptionforcallofevidence', 'requestreports', 'descriptionforrequstreport', 'orderforinvestigation', 'orderforinvestigationdescription']


class AdmissibilityUpdateForm(forms.ModelForm):
    def boolean_coerce(value):
        # value is received as a unicode string
        if str(value).lower() in ('1', 'true'):
            return True
        elif str(value).lower() in ('0', 'false'):
            return False

    petitioner = forms.ModelChoiceField(label='Choose Petitioner',queryset=PetitionForm.objects.filter(anypendingcourtmatter=False), widget=forms.Select(attrs={'class': 'form-control'}))

    admissability = forms.TypedChoiceField(
        label='Do you wish to render the this petition ADMISSIBLE?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    hearingdate = forms.DateField(required=False, label='If yes, Hear the petition taking into account the criteria provided in Section 22 of the '
                                                        'Power of Mercy Act, 2011 on the following date',
                                               widget=forms.DateInput(format=('%m/%d/%Y'),
                                                                      attrs={'class': 'datepicker form-control'}))
    inadmissibilityreason = forms.CharField(required=False, label='If no, give a reason why it is  INADMISSIBLE',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    callforevidence = forms.TypedChoiceField(
        label='Do you wish to call for more evidence?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    descriptionforcallofevidence =  forms.CharField(required=False, label='if yes, please explain',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    requestreports =  forms.TypedChoiceField(
        label='Do you wish to Request reports from various Goverrment Agencies?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    descriptionforrequstreport = forms.CharField(required=False, label='if yes, please list the Government Agencies',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    orderforinvestigation = forms.TypedChoiceField(
        label='Do you wish to order for more investigations?',
        coerce=boolean_coerce,
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left: 30px;'}), )
    orderforinvestigationdescription = forms.CharField(required=False, label='if yes, please explain',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = AdmissibilityForm
        fields = [ 'petitioner','admissability', 'hearingdate', 'inadmissibilityreason', 'callforevidence', 'descriptionforcallofevidence', 'requestreports', 'descriptionforrequstreport', 'orderforinvestigation', 'orderforinvestigationdescription']

class PetitionSummaryForm(forms.ModelForm):
    admissibility = forms.ModelChoiceField(label='Select the Petitioner', queryset=AdmissibilityForm.objects.filter(admissability=True).filter(petitionsummary__isnull=True), widget=forms.Select(attrs={'class': 'form-control'}))
    typeandcircumstancesofoffence = forms.CharField(label='Type and circumstances of the offence', widget=forms.Textarea(attrs={'rows':12,'class':'form-control'}))
    petitionoverview = forms.CharField(label='Petition overview', widget=forms.Textarea(attrs={'rows':12,'class':'form-control'}))
    class Meta:
        model = PetitionSummary
        fields = ['admissibility','typeandcircumstancesofoffence', 'petitionoverview']

class PetitionSummaryEditForm(forms.ModelForm):
    admissibility = forms.ModelChoiceField(label='Select the Petitioner', queryset=AdmissibilityForm.objects.filter(admissability=True), widget=forms.Select(attrs={'class': 'form-control'}))
    typeandcircumstancesofoffence = forms.CharField(label='Type and circumstances of the offence', widget=forms.Textarea(attrs={'rows':12,'class':'form-control'}))
    petitionoverview = forms.CharField(label='Petition overview', widget=forms.Textarea(attrs={'rows':12,'class':'form-control'}))
    class Meta:
        model = PetitionSummary
        fields = ['admissibility','typeandcircumstancesofoffence', 'petitionoverview']


class HearingSummaryForm(forms.ModelForm):
    admissibility = forms.ModelChoiceField(label='Choose Petitioner',queryset=AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull=False).filter(hearing__isnull=True).filter(petitioner__exit__isnull=True), widget=forms.Select(attrs={'class': 'form-control'}))
    healthstatus = forms.CharField(required=False, label='Health Status',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    familystatus = forms.CharField(required=False, label='Family Status (parents, spouse,children etc)',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    natureandseriousnessoftheoffense = forms.CharField(required=False, label='The nature and seriousness of the offense  )',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    personalcircumstances = forms.CharField(required=False, label='The personal circumstances of the offender at the time of making the petition, '
                                                                  'including mental and physical health and any disabilities',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    interestofstateandcommunity = forms.CharField(required=False, label='The interest of State and Community',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    postconvictionconduct = forms.CharField(required=False, label='The post conviction conduct, character and reputation of the convicted criminal prisoner',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    officialrecommendationsandreports = forms.CharField(required=False, label='The official recommendations and reports from State organ or '
                                                                              'department responsible fro correctional services',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    wherethepetitionerhaspersued = forms.CharField(required=False, label='Where the petitioner has opted to pursue other available remedies, the outcome'
                                                                         'of such avenues',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    representationofvictim = forms.CharField(required=False, label='The representation of the victim where applicable',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reportoffellowinmates = forms.CharField(required=False, label='Where applicable, a report of fellow inmates',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reportsfromprobationservices = forms.CharField(required=False, label='Reports from probational services',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    observationswithmainreasons = forms.CharField(required=False, label='Observations with main reasons',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    action = forms.CharField(label='Action',
                                   widget=forms.Select(choices=[('',' Take the action appropriately'),('Interview the Petitioner','Interview the Petitioner'),
                                                                ('Defer the petition to a later date', 'Defer the petition to a later date'),
                                                                ('Decline the Petition', 'Decline the Petition')],
                                                       attrs={'class': 'form-control'}))
    interviewdate = forms.DateField(required=False, label='Set the Interview to take place on', widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control datepicker'}))
    deferdate = forms.DateField(required=False, label='If you choose to Defer the Petion, set the Review Date', widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control datepicker'}))
    actiondescription = forms.CharField(required=False, label='Describe your Action ',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    member1 = forms.CharField(required=False, label='Member 1 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member2 = forms.CharField(required=False, label='Member 2 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member3 = forms.CharField(required=False, label='Member 3 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member4 = forms.CharField(required=False, label='Member 4 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member5 = forms.CharField(required=False, label='Member 5 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member6 = forms.CharField(required=False, label='Member 6 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member7 = forms.CharField(required=False, label='Member 7 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member8 = forms.CharField(required=False, label='Member 8 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member9 = forms.CharField(required=False, label='Member 9 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))
    member10 = forms.CharField(required=False, label='Member 10 Present', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = HearingSummary
        fields = ['admissibility','healthstatus','familystatus','natureandseriousnessoftheoffense', 'personalcircumstances', 'interestofstateandcommunity', 'postconvictionconduct',
                      'officialrecommendationsandreports', 'wherethepetitionerhaspersued', 'representationofvictim',
                      'reportoffellowinmates', 'reportsfromprobationservices', 'observationswithmainreasons','action',
                  'interviewdate','deferdate','actiondescription','member1','member2','member3','member4','member5','member6','member7','member8','member9','member10' ]

class HearingSummaryUpdateForm(forms.ModelForm):
    admissibility = forms.ModelChoiceField(label='Choose Petitioner',queryset=AdmissibilityForm.objects.filter(admissability=True), widget=forms.Select(attrs={'class': 'form-control','readonly':True}))
    healthstatus = forms.CharField(required=False, label='Health Status',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    familystatus = forms.CharField(required=False, label='Family Status (parents, spouse,children etc)',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    natureandseriousnessoftheoffense = forms.CharField(required=False, label='The nature and seriousness of the offense  )',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    personalcircumstances = forms.CharField(required=False, label='The personal circumstances of the offender at the time of making the petition, '
                                                                  'including mental and physical health and any disabilities',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    interestofstateandcommunity = forms.CharField(required=False, label='The interest of State and Community',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    postconvictionconduct = forms.CharField(required=False, label='The post conviction conduct, character and reputation of the convicted criminal prisoner',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    officialrecommendationsandreports = forms.CharField(required=False, label='The official recommendations and reports from State organ or '
                                                                              'department responsible fro correctional services',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    wherethepetitionerhaspersued = forms.CharField(required=False, label='Where the petitioner has opted to pursue other available remedies, the outcome'
                                                                         'of such avenues',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    representationofvictim = forms.CharField(required=False, label='The representation of the victim where applicable',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reportoffellowinmates = forms.CharField(required=False, label='Where applicable, a report of fellow inmates',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reportsfromprobationservices = forms.CharField(required=False, label='Reports from probational services',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    observationswithmainreasons = forms.CharField(required=False, label='Observations with main reasons',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    action = forms.CharField(label='Action',
                                   widget=forms.Select(choices=[('',' Take the action appropriately'),('Interview the Petitioner','Interview the Petitioner'),
                                                                ('Defer the petition to a later date', 'Defer the petition to a later date'),
                                                                ('Decline the Petition', 'Decline the Petition')],
                                                       attrs={'class': 'form-control'}))
    interviewdate = forms.DateField(required=False, label='Set the Interview to take place on', widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control datepicker'}))
    deferdate = forms.DateField(required=False, label='If you choose to Defer the Petion, set the Review Date', widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control datepicker'}))
    actiondescription = forms.CharField(required=False, label='Describe your Action ',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    member1 = forms.CharField(required=False, label='Member 1 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member2 = forms.CharField(required=False, label='Member 2 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member3 = forms.CharField(required=False, label='Member 3 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member4 = forms.CharField(required=False, label='Member 4 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member5 = forms.CharField(required=False, label='Member 5 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member6 = forms.CharField(required=False, label='Member 6 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member7 = forms.CharField(required=False, label='Member 7 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member8 = forms.CharField(required=False, label='Member 8 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member9 = forms.CharField(required=False, label='Member 9 Present',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    member10 = forms.CharField(required=False, label='Member 10 Present',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = HearingSummary
        fields = ['admissibility','healthstatus','familystatus','natureandseriousnessoftheoffense', 'personalcircumstances', 'interestofstateandcommunity', 'postconvictionconduct',
                      'officialrecommendationsandreports', 'wherethepetitionerhaspersued', 'representationofvictim',
                      'reportoffellowinmates', 'reportsfromprobationservices', 'observationswithmainreasons','action',
                  'interviewdate','deferdate','actiondescription','member1','member2','member3','member4','member5','member6','member7','member8','member9','member10' ]

class InterviewSummaryForm(forms.ModelForm):

    def boolean_coerce(value):
        # value is received as a unicode string
        if str(value).lower() in ('1', 'true'):
            return True
        elif str(value).lower() in ('0', 'false'):
            return False

    hearing = forms.ModelChoiceField(label='Select the Petitioner', queryset= HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull=False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True),widget=forms.Select(attrs={'class':'form-control'}))
    ownaccountofcircumstances = forms.CharField(required=False, label='Own account of circumstances sorrounding the commission of Offense ',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reconciliationefforts = forms.CharField(required=False, label='Reconciliation efforts with the victims of the offense that led to current conviction ',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    indicationofremosefulness =forms.CharField(required=False, label='Indication of remosefulness or otherwise',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    anyothercomments = forms.CharField(required=False, label=' Any other comments',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    representationofthevictim = forms.CharField(required=False, label='Representation of the victim (if applicable) ',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    concludingobservations  = forms.CharField(label='Concluding Observations of major Members in view of the hearing and Interviews conducted in the Petition',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    chairpersonvote = forms.TypedChoiceField(required=True,
        label='Chairpersons Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    chairpersonvotereason= forms.CharField(required=False, label='Chairpersons Remarks for the vote',
                                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    vicechairvote = forms.TypedChoiceField(required=True,
        label='Vice Chairpersons Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    vicechairvotereason = forms.CharField(required=False, label='Vice Chairpersons Remarks for the vote',
                                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    csvote = forms.TypedChoiceField(required=True,
        label='Cabinet Secretary\'s (Interior) Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    csvotereason = forms.CharField(required=False, label='Cabinet Secretary\'s Remarks for the vote',
                                          widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m1vote = forms.TypedChoiceField(required=True,
        label='Member 1\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m1votereason = forms.CharField(required=False, label='Member 1\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m2vote = forms.TypedChoiceField(required=True,
        label='Member 2\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m2votereason = forms.CharField(required=False, label='Member 2\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m3vote = forms.TypedChoiceField(required=True,
        label='Member 3\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m3votereason = forms.CharField(required=False, label='Member 3\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m4vote = forms.TypedChoiceField(required=True,
        label='Member 4\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m4votereason = forms.CharField(required=False, label='Member 4\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m5vote = forms.TypedChoiceField(required=True,
        label='Member 5\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m5votereason = forms.CharField(required=False, label='Member 5\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m6vote = forms.TypedChoiceField(required=True,
        label='Member 6\'s Vote',
        coerce=boolean_coerce,
        choices=((True, 'Recommend to President'), (False, 'Not Recommended to President')),
        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m6votereason = forms.CharField(required=False, label='Member 6\'s Remarks for the vote',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    finalresolution = forms.CharField(label='FINAL RESOLUTION',
                                   widget=forms.Select(choices=[('','Choose Appropritely'),('Recommended to President','Recommended to President'),
                                                                ('Not Recommended to President', 'Not Recommended to President')],
                                                       attrs={'class': 'form-control'}))
    class Meta:
        model = InterviewSummary
        fields = ['hearing','ownaccountofcircumstances', 'reconciliationefforts', 'indicationofremosefulness',
                      'anyothercomments', 'representationofthevictim', 'concludingobservations', 'chairpersonvote',
                      'chairpersonvotereason', 'vicechairvote', 'vicechairvotereason', 'csvote', 'csvotereason',
                      'm1vote', 'm1votereason','m2vote', 'm2votereason','m3vote', 'm3votereason','m4vote', 'm4votereason',
                  'm5vote', 'm5votereason','m6vote', 'm6votereason','finalresolution']


class InterviewSummaryEditForm(forms.ModelForm):

    def boolean_coerce(value):
            # value is received as a unicode string
            if str(value).lower() in ('1', 'true'):
                return True
            elif str(value).lower() in ('0', 'false'):
                return False

    hearing = forms.ModelChoiceField(label='Select the Petitioner', queryset=HearingSummary.objects.filter(
            action='Interview the Petitioner').filter(interviewdate__isnull=False), widget=forms.Select(attrs={'class': 'form-control'}))
    ownaccountofcircumstances = forms.CharField(required=False,
                                                    label='Own account of circumstances sorrounding the commission of Offense ',
                                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    reconciliationefforts = forms.CharField(required=False,
                                                label='Reconciliation efforts with the victims of the offense that led to current conviction ',
                                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    indicationofremosefulness = forms.CharField(required=False, label='Indication of remosefulness or otherwise',
                                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    anyothercomments = forms.CharField(required=False, label=' Any other comments',
                                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    representationofthevictim = forms.CharField(required=False,
                                                    label='Representation of the victim (if applicable) ',
                                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    concludingobservations = forms.CharField(
            label='Concluding Observations of major Members in view of the hearing and Interviews conducted in the Petition',
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    chairpersonvote = forms.TypedChoiceField(required=True,
                                                 label='Chairpersons Vote',
                                                 coerce=boolean_coerce,
                                                 choices=((True, 'Recommend to President'),
                                                          (False, 'Not Recommended to President')),
                                                 widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    chairpersonvotereason = forms.CharField(required=False, label='Chairpersons Remarks for the vote',
                                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    vicechairvote = forms.TypedChoiceField(required=True,
                                               label='Chairpersons Vote',
                                               coerce=boolean_coerce,
                                               choices=((True, 'Recommend to President'),
                                                        (False, 'Not Recommended to President')),
                                               widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    vicechairvotereason = forms.CharField(required=False, label='Vice Chairpersons Remarks for the vote',
                                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    csvote = forms.TypedChoiceField(required=True,
                                        label='Cabinet Secretary\'s (Interior) Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    csvotereason = forms.CharField(required=False, label='Cabinet Secretary\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m1vote = forms.TypedChoiceField(required=True,
                                        label='Member 1\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m1votereason = forms.CharField(required=False, label='Member 1\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m2vote = forms.TypedChoiceField(required=True,
                                        label='Member 2\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m2votereason = forms.CharField(required=False, label='Member 2\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m3vote = forms.TypedChoiceField(required=True,
                                        label='Member 3\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m3votereason = forms.CharField(required=False, label='Member 3\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m4vote = forms.TypedChoiceField(required=True,
                                        label='Member 4\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m4votereason = forms.CharField(required=False, label='Member 4\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m5vote = forms.TypedChoiceField(required=True,
                                        label='Member 5\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m5votereason = forms.CharField(required=False, label='Member 5\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    m6vote = forms.TypedChoiceField(required=True,
                                        label='Member 6\'s Vote',
                                        coerce=boolean_coerce,
                                        choices=(
                                        (True, 'Recommend to President'), (False, 'Not Recommended to President')),
                                        widget=forms.RadioSelect(attrs={'style': 'margin-left:-15px;'}), )
    m6votereason = forms.CharField(required=False, label='Member 6\'s Remarks for the vote',
                                       widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    finalresolution = forms.CharField(label='FINAL RESOLUTION',
                                          widget=forms.Select(choices=[('', 'Choose Appropritely'), (
                                          'Recommended to President', 'Recommended to President'),
                                                                       ('Not Recommended to President',
                                                                        'Not Recommended to President')],
                                                              attrs={'class': 'form-control'}))

    class Meta:
        model = InterviewSummary
        fields = ['hearing','ownaccountofcircumstances', 'reconciliationefforts', 'indicationofremosefulness',
                      'anyothercomments', 'representationofthevictim', 'concludingobservations', 'chairpersonvote',
                      'chairpersonvotereason', 'vicechairvote', 'vicechairvotereason', 'csvote', 'csvotereason',
                      'm1vote', 'm1votereason','m2vote', 'm2votereason','m3vote', 'm3votereason','m4vote', 'm4votereason',
                  'm5vote', 'm5votereason','m6vote', 'm6votereason','finalresolution']

class RecommendationFormForm(forms.ModelForm):
    interview = forms.ModelChoiceField(label='Select the Petitioner', queryset= InterviewSummary.objects.filter(finalresolution= 'Recommended to President').filter(recommendationform__isnull= True).filter(hearing__admissibility__petitioner__exit__isnull=True),widget=forms.Select(attrs={'class':'form-control'}))
    explanationofrecommedation = forms.CharField(required=True, label='Following the investigations conducted, evidence gathered, interviews held and '
                                                                       'consideration of the reports from appropriate Government agencis, the Committee forms the opinion that the Petitioner: ',
                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    mercy = forms.CharField(label='His Excellency the President to exercise the power of mercy by',
                                          widget=forms.Select(choices=[('', 'Choose Appropritely'), (
                                          'granting a free or conditional pardon to a person convicted of an office', 'granting a free or conditional pardon to a person convicted of an office'),
                                        ('postponing the carrying out of a punishment, either for a specified or indefinite period','postponing the carrying out of a punishment, either for a specified or indefinite period'),
                                        ('substituting a less severe form of punishment','substituting a less severe form of punishment'),
                                        ('remitting all or part of a punishment','remitting all or part of a punishment')
                                                                       ],
                                                              attrs={'class': 'form-control'}))
    circumstanceofoffence = forms.CharField(required=False,
                                                 label='Circumstances sorrounding the commission of the offence',
                                                 widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    compellingremarks = forms.CharField(required=False,
                                            label='Compelling Recommendation Remarks',
                                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    class Meta:
        model = RecommendationForm
        fields = ['interview','mercy','explanationofrecommedation' ,'circumstanceofoffence','compellingremarks']

class RecommendationUpdateForm(forms.ModelForm):
    def boolean_coerce(value):
        # value is received as a unicode string
        if str(value).lower() in ('1', 'true'):
            return True
        elif str(value).lower() in ('0', 'false'):
            return False
    interview = forms.ModelChoiceField(label='Select the Petitioner', queryset= InterviewSummary.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    explanationofrecommedation = forms.CharField(required=True, label='Following the investigations conducted, evidence gathered, interviews held and '
                                                                       'consideration of the reports from appropriate Government agencis, the Committee forms the opinion that the Petitioner: ',
                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    mercy = forms.CharField(label='His Excellency the President to exercise the power of mercy by',
                            widget=forms.Select(choices=[('', 'Choose Appropritely'), (
                                'granting a free or conditional pardon to a person convicted of an office',
                                'granting a free or conditional pardon to a person convicted of an office'),
                                                         (
                                                         'postponing the carrying out of a punishment, either for a specified or indefinite period',
                                                         'postponing the carrying out of a punishment, either for a specified or indefinite period'),
                                                         ('substituting a less severe form of punishment',
                                                          'substituting a less severe form of punishment'),
                                                         ('remitting all or part of a punishment',
                                                          'remitting all or part of a punishment')
                                                         ],
                                                attrs={'class': 'form-control'}))
    circumstanceofoffence = forms.CharField(required=False,
                                            label='Circumstances sorrounding the commission of the offence',
                                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    compellingremarks = forms.CharField(required=False,
                                        label='Compelling Recommendation Remarks',
                                        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))

    class Meta:
        model = RecommendationForm
        fields = ['interview', 'mercy','explanationofrecommedation','circumstanceofoffence','compellingremarks' ]


class ExitForm(forms.ModelForm):
    exitreason = forms.CharField(label='Reason why the petitioner exited the prison',
                                 widget=forms.Select(choices=[('', 'Choose Appropritely'), (
                                     'Released under POMAC',
                                     'Released under POMAC'),
                                                              (
                                                                  'Released after serving the term',
                                                                  'Released after serving the term'),
                                                              ('The Petitioner escaped the prison',
                                                               'The Petitioner escaped the prison'),
                                                              ('The petitioner died',
                                                               'The petitioner died'),
                                                              ('The petitioner was released after resentencing',
                                                               'The petitioner was released after resentencing')
                                                              ],
                                                     attrs={'class': 'form-control'}))
    petitioner = forms.ModelChoiceField(queryset=PetitionForm.objects.all().filter(exit__isnull=True),
                                        label='Choose Petitioner',
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Exit
        fields = [ 'petitioner','exitreason']

class GrantForm(forms.ModelForm):
    recommendation = forms.ModelChoiceField(queryset=RecommendationForm.objects.all().filter(grant__isnull=True).filter(interview__hearing__admissibility__petitioner__exit__isnull=True),
                                            label='Choose Petitioner', widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Grant
        fields = ['recommendation']

class ExitFormUpdate(forms.ModelForm):
    exitreason = forms.CharField(label='Reason why the petitioner exited the prison',
                                 widget=forms.Select(choices=[('', 'Choose Appropritely'), (
                                     'Released under POMAC',
                                     'Released under POMAC'),
                                                              (
                                                                  'Released after serving the term',
                                                                  'Released after serving the term'),
                                                              ('The Petitioner escaped the prison',
                                                               'The Petitioner escaped the prison'),
                                                              ('The petitioner died while in prison',
                                                               'The petitioner died while in prison'),
                                                              ('The petitioner was released after resentencing',
                                                               'The petitioner was released after resentencing')
                                                              ],
                                                     attrs={'class': 'form-control'}))
    petitioner = forms.ModelChoiceField(queryset=PetitionForm.objects.all(),
                                        label='Choose Petitioner',
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Exit
        fields = [ 'petitioner','exitreason']