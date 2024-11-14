from datetime import datetime

from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False,
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='active',
        default=True,
    )

    class Meta:
        abstract = True
        managed = True


class Organizer(ModelBase):
    name = models.CharField(
        max_length=100,
        db_column='name_organizer',
        null=False,
    )
    cpf = models.CharField(
        max_length=10,
        db_column='cpf_organizer',
        null=False,
    )
    email = models.EmailField(
        db_column='email_organizer',
        null=False,
    )

    class Meta:
        db_table = 'Organizer'
        managed = True


class Event(ModelBase):
    title = models.CharField(
        max_length=100,
        db_column='title',
        null=False,
    )
    description = models.CharField(
        max_length=255,
        db_column='description',
        null=False,
    )
    date_time = models.DateTimeField(
        db_column='date_time',
        null=False,
    )
    location = models.CharField(
        db_column='location',
        max_length=255,
        null=False,
    )
    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.PROTECT,
        db_column='organizer',
        null=False,
    )
    max_participants = models.IntegerField(
        db_column='max_participants',
        null=False,
    )
    participants_count = models.IntegerField(
        db_column='participants_count',
        default=0,
    )

    class Meta:
        db_table = 'Event'
        managed = True


class Participant(ModelBase):
    name = models.CharField(
        max_length=100,
        db_column='name_participant',
        null=False,
    )
    cpf = models.CharField(
        max_length=10,
        db_column='cpf_participant',
        null=False,
    )
    email = models.EmailField(
        db_column='email_participant',
        null=False,
    )
    go_event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        db_column='go_event',
        null=False,
    )

    class Meta:
        db_table = 'Participant'
        managed = True
