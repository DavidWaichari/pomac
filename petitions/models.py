from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django.utils.timezone import now

class County(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False,)
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
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL) #relationship

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


class Prison(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_prison_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_prison_update', args=(self.pk,))

    def __str__(self):
        return self.name

class Court(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_court_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_court_update', args=(self.pk,))

    def __str__(self):
        return self.name


class Offence(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_offence_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_offence_update', args=(self.pk,))

    def __str__(self):
        return self.name


class PetitionForm(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    selectnationality = models.BooleanField()
    nationality = models.CharField(max_length=30, null=True)
    prison = models.ForeignKey(Prison,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    prisonno = models.CharField(max_length=30, unique=True)
    court = models.ForeignKey(Court,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    courtcaseno = models.CharField(max_length=10)
    dateofconviction = models.DateField()
    dateofcustody = models.DateField()
    ageatconviction = models.IntegerField()
    agewhenoffensewascommited = models.IntegerField()
    county = models.ForeignKey(County,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    subcounty = models.ForeignKey(SubCounty,
                                 null=True, blank=True, on_delete=models.SET_NULL)
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
    offence = models.ForeignKey(Offence,
                                 null=True, blank=True, on_delete=models.SET_NULL)
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
    isttheapplicantthepetitioner = models.BooleanField()
    nameofapplicant = models.CharField(max_length=255,null=True)
    relationshipofapplicantwithpetitioner = models.CharField(max_length=255,null=True)
    addressoftheapplicant = models.CharField(max_length=255,null=True)
    telephonenumberoftheapplicant = models.CharField(max_length=255,null=True)
    created = models.DateTimeField(default=now, editable=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_by')

    class Meta:
        permissions = (
            ('can_view_petitionforms', 'User can view all petitions'),
            ('can_view_mypetitionforms', 'User can view all my petitions'),
            ('can_view_petitionformstatus', 'User can view the status of petitions'),
            ('can_view_duplicatesfinder', 'User can view the petitions duplicates'),
            ('can_view_petitionformdetails', 'User can view the details of petitions'),
            ('can_view_main_dashboard', 'User can view main dashboard'),
            ('can_view_more_reports', 'User can view more reports dashboard'),
            ('can_modifydates_created', 'User can modify dates of creation/submission'),
        )
        ordering = ('-created',)

    def permission_required(*perms):
        return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/')

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitionform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitionform_update', args=(self.pk,))

    def __str__(self):
        return self.name+" | "+self.prisonno+" | "+self.prison.name




class AdmissibilityForm(models.Model):
    # Fields
    created = models.DateTimeField(default=now, editable=True)
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
    petitioner = models.OneToOneField(PetitionForm, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='admissibility_updated_by')
    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_admissibilityform', 'User can view all admissibilities'),
            ('can_view_myadmissibilityform', 'User can view all my admissibilities'),
            ('can_print_admissibilityform', 'User can print admissibility form'),
            ('can_view_admissibilityformdetails', 'User can view details of admissibility'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('admissibilityform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('admissibilityform_update', args=(self.pk,))

    def __str__(self):
        return self.petitioner.name+'  |  '+self.petitioner.prisonno+'  |  '+self.petitioner.prison.name




class PetitionSummary(models.Model):

    # Fields
    typeandcircumstancesofoffence = models.TextField(max_length=1000)
    petitionoverview = models.TextField(max_length=1000)
    created = models.DateTimeField(default=now, editable=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    admissibility = models.ForeignKey(AdmissibilityForm, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='summary_updated_by')

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_petitionsummary', 'User can view all summaries'),
            ('can_view_mypetitionsummary', 'User can view all my summaries'),
            ('can_view_petitionsummarydetails', 'User can view all petition summary details'),
            ('can_print_petitionsummary', 'User can print the petition summary'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitionsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitionsummary_update', args=(self.pk,))


class HearingSummary(models.Model):

    # Fields
    created = models.DateTimeField(default=now, editable=True)
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
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='hearing_updated_by')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["admissibility"]
        else:
            return []

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_hearingsummaries', 'User can view all hearings'),
            ('can_view_myhearings', 'User can view all his/her hearings'),
            ('can_print_hearing', 'User can print hearing summary form'),
            ('can_view_hearingdetails', 'User can view details of a hearing'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('hearingsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('hearingsummary_update', args=(self.pk,))

    def __str__(self):
        return self.admissibility.petitioner.name + ' | ' + self.admissibility.petitioner.prisonno + ' | ' + self.admissibility.petitioner.prison.name


class InterviewSummary(models.Model):
    # Fields
    created = models.DateTimeField(default=now, editable=True)
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
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='interview_updated_by')

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_interviews', 'User can view all interviews'),
            ('can_view_myinterviews', 'User can view all his/her interviews'),
            ('can_print_interviews', 'User can print hearing interview summary'),
            ('can_view_interviewdetails', 'User can view details of an interview'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('interviewsummary_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('interviewsummary_update', args=(self.pk,))

    def __str__(self):
        return self.hearing.admissibility.petitioner.name+ ' '+self.hearing.admissibility.petitioner.prisonno+ ' '+self.hearing.admissibility.petitioner.prison.name


class RecommendationForm(models.Model):

    # Fields
    created = models.DateTimeField(default=now, editable=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    explanationofrecommedation = models.TextField(max_length=1000)
    mercy = models.CharField(max_length=200)
    circumstanceofoffence = models.TextField(max_length=1500, null=True)
    compellingremarks = models.TextField(max_length=1500, null=True)
    # Relationship Fields
    interview = models.OneToOneField(InterviewSummary,on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='recommendation_updated_by')

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_recommendations', 'User can view all recommendations'),
            ('can_view_myrecommendations', 'User can view all his/her recommendations'),
            ('can_print_recommendations', 'User can  print a recommendation'),
            ('can_view_recommendationdetails', 'User can view details of a recommendation'),
            ('can_view_master_recommendations', 'User can view master_recommendations'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('recommendationform_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('recommendationform_update', args=(self.pk,))
    def __str__(self):
        return self.interview.hearing.admissibility.petitioner.name+ ' '+self.interview.hearing.admissibility.petitioner.prisonno+ ' '+self.interview.hearing.admissibility.petitioner.prison.name

class Grant(models.Model):

    # Fields
    created = models.DateTimeField(default=now, editable=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    recommendation = models.ForeignKey(RecommendationForm,on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='grant_updated_by')

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_grants', 'User can view all the grant of petitions'),
            ('can_view_mygrants', 'User can view all his/her grants of petitions'),
            ('can_print_grants', 'User can  print a grant'),
            ('can_view_grantdetails', 'User can view details of a grant'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_grant_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_grant_update', args=(self.pk,))



class Exit(models.Model):

    # Fields
    created = models.DateTimeField(default=now, editable=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    exitreason = models.CharField(max_length=100)
    exitdate = models.DateField(null=True, blank=True)

    # Relationship Fields
    petitioner = models.OneToOneField(PetitionForm, on_delete=models.CASCADE, related_name='exit')

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='exit_updated_by')

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('can_view_exits', 'User can view all the petitioners who have exited'),
            ('can_view_exitdetails', 'User can view details of a grant'),
        )

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('petitions_exit_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('petitions_exit_update', args=(self.pk,))

    def __str__(self):
        return self.petitioner.name+ ' '+self.petitioner.prisonno+ ' '+self.petitioner.prison.name