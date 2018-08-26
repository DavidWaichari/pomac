from django.urls import reverse
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models

class County(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_county_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_county_update', args=(self.pk,))

    def __str__(self):
        return self.name



class SubCounty(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    # Relationship Fields
    county = models.ForeignKey(County,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_subcounty_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_subcounty_update', args=(self.pk,))

    def __str__(self):
        return self.name


class PetitionForm(models.Model):
    from petitions.models import County, SubCounty
    # Fields
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=30)
    prison = models.CharField(max_length=50)
    prisonno = models.CharField(max_length=30, unique=True)
    court = models.CharField(max_length=50)
    courtcaseno = models.CharField(max_length=30)
    dateofconviction = models.DateField()
    dateofcustody = models.DateField()
    ageatconviction = models.IntegerField()
    agewhenoffensewascommited = models.IntegerField()
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    subcounty = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    nextofkin = models.CharField(max_length=50)
    relationshipwithnextofkin = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=50)
    telnoofcontactperson = models.CharField(max_length=15)
    nearestschool = models.CharField(max_length=50)
    homechief = models.CharField(max_length=30)
    whereoffensewascommitted = models.CharField(max_length=50, )
    convictedforlife = models.BooleanField()
    sentence = models.IntegerField(null=True, blank= True)
    reliefsought = models.CharField(max_length=100)
    offence = models.CharField(max_length=100)
    natureandparticularsofoffense = models.TextField(max_length=500)
    chargedalonefortheoffense = models.BooleanField()
    namesofcoaccused = models.TextField(max_length=100)
    knowledgeofthevictim = models.BooleanField()
    nameofvictim = models.CharField(max_length=30)
    areaofresidence = models.CharField(max_length=30)
    previousconvictions = models.TextField(max_length=300)
    previouspetition = models.BooleanField()
    dateofpreviouspetition = models.DateField(null=True)
    reasonofdenialofpreviouspetition = models.TextField(max_length=100)
    reasonforcurrentpetition = models.TextField(max_length=300)
    anydisplinaryactioninprison = models.BooleanField()
    detailsofdisplinaryactioninprison = models.TextField(max_length=300)
    anyspecialcondition = models.BooleanField()
    detailsofspecialcondition = models.TextField(max_length=100)
    areyouatrustee = models.BooleanField()
    dateofpromotiontotrustee = models.DateField(null=True)
    anyspecialattributesorskills = models.BooleanField()
    explanationofspecialattributesorskills = models.TextField(max_length=300)
    appealedagainsttheconviction = models.BooleanField()
    appealcaseno = models.CharField(max_length=30)
    appealoutcome = models.TextField(max_length=100)
    anypendingcourtmatter = models.BooleanField()
    explanationofpendingcourtmatter = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitionform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitionform_update', args=(self.pk,))

    def __str__(self):
        return self.name+" | "+self.prisonno+" | "+self.prison



class AdmissibilityForm(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    admissability = models.BooleanField()
    hearingdate = models.DateField(null=True, blank= True)
    inadmissibilityreason = models.TextField(max_length=300, null=True, blank=True)
    callforevidence = models.BooleanField()
    descriptionforcallofevidence = models.TextField(max_length=300, null=True, blank= True)
    requestreports = models.BooleanField()
    descriptionforrequstreport = models.TextField(max_length=300, null=True, blank= True)
    orderforinvestigation = models.BooleanField()
    orderforinvestigationdescription = models.TextField(max_length=300,null=True, blank= True)

    # Relationship Fields
    petitioner = models.OneToOneField(PetitionForm, on_delete=models.CASCADE, related_name='admissibility')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('admissibilityform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('admissibilityform_update', args=(self.pk,))

    def __str__(self):
        return self.petitioner.name+'  |  '+self.petitioner.prisonno+'  |  '+self.petitioner.prison




class PetitionSummary(models.Model):

    # Fields
    typeandcircumstancesofoffence = models.TextField(max_length=1000)
    petitionoverview = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    admissibility = models.ForeignKey(AdmissibilityForm, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitionsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitionsummary_update', args=(self.pk,))


class HearingSummary(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    healthstatus = models.TextField(max_length=400)
    familystatus = models.TextField(max_length=400)
    natureandseriousnessoftheoffense = models.TextField(max_length=400)
    personalcircumstances = models.TextField(max_length=400)
    interestofstateandcommunity = models.TextField(max_length=400)
    postconvictionconduct = models.TextField(max_length=400)
    officialrecommendationsandreports = models.TextField(max_length=400)
    wherethepetitionerhaspersued = models.TextField(max_length=400)
    representationofvictim = models.TextField(max_length=400)
    reportoffellowinmates = models.TextField(max_length=400)
    reportsfromprobationservices = models.TextField(max_length=1000)
    observationswithmainreasons = models.TextField(max_length=1000)
    action = models.CharField(max_length=100)
    interviewdate = models.DateField(null=True, blank=True)
    reviewdate = models.DateField(null=True, blank=True)
    actiondescription = models.TextField(max_length=400)
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    member3 = models.CharField(max_length=100)
    member4 = models.CharField(max_length=100)
    member5 = models.CharField(max_length=100)
    member6 = models.CharField(max_length=100)
    member7 = models.CharField(max_length=100)
    member8 = models.CharField(max_length=100)
    member9 = models.CharField(max_length=100)
    member10 = models.CharField(max_length=100)

    # Relationship Fields
    admissibility = models.OneToOneField(AdmissibilityForm,on_delete=models.CASCADE, related_name='hearing')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["admissibility"]
        else:
            return []

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('hearingsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('hearingsummary_update', args=(self.pk,))

    def __str__(self):
        return self.admissibility.petitioner.name + ' | ' + self.admissibility.petitioner.prisonno + ' | ' + self.admissibility.petitioner.prison


class InterviewSummary(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    ownaccountofcircumstances = models.TextField(max_length=1000)
    reconciliationefforts = models.TextField(max_length=1000)
    indicationofremosefulness = models.TextField(max_length=1000)
    anyothercomments = models.TextField(max_length=1000)
    representationofthevictim = models.TextField(max_length=100)
    concludingobservations = models.TextField(max_length=1000)
    chairpersonvote = models.BooleanField()
    chairpersonvotereason = models.TextField(max_length=300)
    vicechairvote = models.BooleanField()
    vicechairvotereason = models.TextField(max_length=100)
    csvote = models.NullBooleanField()
    csvotereason = models.TextField(max_length=100)
    m1vote = models.NullBooleanField()
    m1votereason = models.TextField(max_length=100)
    m2vote = models.NullBooleanField()
    m2votereason = models.TextField(max_length=100)
    m3vote = models.NullBooleanField()
    m3votereason = models.TextField(max_length=100)
    m4vote = models.NullBooleanField()
    m4votereason = models.TextField(max_length=100)
    m5vote = models.NullBooleanField()
    m5votereason = models.TextField(max_length=100)
    m6vote = models.NullBooleanField()
    m6votereason = models.TextField(max_length=100)
    finalresolution = models.CharField(max_length=30)
    hearing = models.OneToOneField(HearingSummary, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('interviewsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('interviewsummary_update', args=(self.pk,))

    def __str__(self):
        return self.hearing.admissibility.petitioner.name+ ' '+self.hearing.admissibility.petitioner.prisonno+ ' '+self.hearing.admissibility.petitioner.prison


class RecommendationForm(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    explanationofrecommedation = models.TextField(max_length=1000)
    mercy = models.CharField(max_length=200)

    # Relationship Fields
    interview = models.OneToOneField(InterviewSummary,on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('recommendationform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('recommendationform_update', args=(self.pk,))
    def __str__(self):
        return self.interview.hearing.admissibility.petitioner.name+ ' '+self.interview.hearing.admissibility.petitioner.prisonno+ ' '+self.interview.hearing.admissibility.petitioner.prison
