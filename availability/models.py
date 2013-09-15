from django.db import models
from club.models import Season, SquadMember
from fixtures.models import Fixture


class AvailabilityDate(models.Model):
    date = models.DateField()
    season = models.ForeignKey(Season)

    class Meta:
        abstract = True


class FixtureDate(AvailabilityDate):
    fixture = models.ForeignKey(Fixture, null=True)


class Answer(models.Model):
    date = models.ForeignKey('FixtureDate')
    player = models.ForeignKey(SquadMember)

    class Meta:
        abstract = True


class YesNoAnswer(Answer):
    yes = models.BooleanField(default=False)


class OptionAnswer(Answer):
    option = models.CharField(max_length=32)
