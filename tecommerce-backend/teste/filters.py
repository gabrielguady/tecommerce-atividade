
from django_filters import rest_framework as filters
from teste import models

class OrganizerFilter(filters.FilterSet):
    class Meta:
        model = models.Organizer
