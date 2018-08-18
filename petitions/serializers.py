from . import models

from rest_framework import serializers


class PetitionFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PetitionForm
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'prisonno', 
            'nationality', 
            'courtcaseno', 
            'ageatconviction', 
            'currentage', 
            'agewhenoffensewascommited', 
            'nextofkin', 
            'relationshipwithnextofkin', 
            'contactperson', 
            'telnoofcontactperson', 
            'location', 
            'nearestschool', 
            'homechief', 
            'whereoffensewascommitted', 
            'dateofconviction', 
            'dateofcustody', 
            'reliefsought', 
            'natureandparticularsofoffense', 
            'chargedalonefortheoffense', 
            'namesofcoaccused', 
            'knowledgeofthevictim', 
            'nameofvictim', 
            'areaofresidence', 
            'previousconvictions', 
            'previouspetition', 
            'dateofpreviouspetition', 
            'reasonofdenialofpreviouspetition', 
            'reasonforcurrentpetition', 
            'anydisplinaryactioninprison', 
            'detailsofdisplinaryactioninprison', 
            'anyspecialcondition', 
            'detailsofspecialcondition', 
            'areyouatrustee', 
            'dateofpromotiontotrustee', 
            'anyspecialattributesorskills', 
            'explanationofspecialattributesorskills', 
            'appealedagainsttheconviction', 
            'appealcaseno', 
            'appealoutcome', 
            'anypendingcourtmatter', 
            'explanationofpendingcourtmatter', 
        )


class CourtSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Court
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


class PrisonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prison
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.County
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


class SubCountySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubCounty
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


