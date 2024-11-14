from rest_framework import routers

from teste import viewSets

router = routers.DefaultRouter()

router.register('organizer', viewSets.OrganizerViewSet)
router.register('event', viewSets.EventViewSet)
router.register('participant', viewSets.ParticipantViewSet)

urlpatterns = router.urls