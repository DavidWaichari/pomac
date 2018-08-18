from . import models
from . import serializers
from rest_framework import viewsets, permissions


class PetitionFormViewSet(viewsets.ModelViewSet):
    """ViewSet for the PetitionForm class"""

    queryset = models.PetitionForm.objects.all()
    serializer_class = serializers.PetitionFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourtViewSet(viewsets.ModelViewSet):
    """ViewSet for the Court class"""

    queryset = models.Court.objects.all()
    serializer_class = serializers.CourtSerializer
    permission_classes = [permissions.IsAuthenticated]


class PrisonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Prison class"""

    queryset = models.Prison.objects.all()
    serializer_class = serializers.PrisonSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountyViewSet(viewsets.ModelViewSet):
    """ViewSet for the County class"""

    queryset = models.County.objects.all()
    serializer_class = serializers.CountySerializer
    permission_classes = [permissions.IsAuthenticated]


class SubCountyViewSet(viewsets.ModelViewSet):
    """ViewSet for the SubCounty class"""

    queryset = models.SubCounty.objects.all()
    serializer_class = serializers.SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]


