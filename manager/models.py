# -*- coding: utf-8 -*-

from django.db import models
from club.models import SquadMember
from fixtures.models import Fixture


class MatchReport(models.Model):
    fixture = models.ForeignKey(Fixture)
    author = models.ForeignKey(SquadMember)
    title = models.CharField(max_length=255, blank=True, null=True)
    report = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return str(self.title)
        else:
            return 'No Title'


class Fine(models.Model):
    fixture = models.ForeignKey(Fixture, null=True, related_name='fines')
    recipient = models.ForeignKey(SquadMember)
    amount = models.IntegerField(default=50)
    reason = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (£%s)" % (str(self.recipient), self.amount/100)


class Prematch(models.Model):
    fixture = models.ForeignKey(Fixture)
    author = models.ForeignKey(SquadMember)
    notes = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255, blank=True)
    beer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.fixture)
