

from teste import models, serializers
from rest_framework import viewsets

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = models.Organizer.objects.all()
    model = models.Organizer
    serializer_class = serializers.OrganizerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    model = models.Event
    serializer_class = serializers.EventSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = models.Participant.objects.all()
    model = models.Participant
    serializer_class = serializers.ParticipantSerializer