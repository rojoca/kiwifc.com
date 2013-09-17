from django.db import models
from club.models import Season, SquadMember


class League(models.Model):
    name = models.CharField(max_length=255)
    season = models.ForeignKey(Season)

    def __str__(self):
        return "%s %s" % (self.name, self.season.name)


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Opponent(models.Model):
    name = models.CharField(max_length=255)
    home_ground = models.ForeignKey('Venue', null=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    start_date = models.DateTimeField(null=True)
    opponent = models.ForeignKey('Opponent')
    venue = models.ForeignKey('Venue', null=True)
    league = models.ForeignKey('League')
    home_game = models.BooleanField(default=True)
    defaulted = models.BooleanField(default=False)
    postponed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    played = models.BooleanField(default=False)
    goals_scored = models.IntegerField(blank=True, null=True)
    goals_conceded = models.IntegerField(blank=True, null=True)
    lineup = models.ManyToManyField(SquadMember, through='Selection')

    def __str__(self):
        if self.start_date:
            date = self.start_date.strftime("%d/%m/%y")
            time = ' at %s' % self.start_date.strftime("%H:%M")
        else:
            date = 'TBD'
            time = ''

        if self.home_game:
            home = 'home'
        else:
            home = 'away'

        return "%s%s vs %s (%s)" % (date, time, self.opponent, home)

    def match_date(self):
        return self.start_date.date()

    def match_time(self):
        return self.start_date.time()

    def result(self):
        if self.played:
            result = 'D'
            if self.goals_conceded > self.goals_scored:
                result = 'L'
            if self.goals_conceded < self.goals_scored:
                result = 'W'
            return result

    def score(self):
        if self.goals_conceded and self.goals_scored:
            return "%s - %s" % (self.goals_scored, self.goals_conceded)


class Selection(models.Model):
    fixture = models.ForeignKey('Fixture')
    squad_member = models.ForeignKey(SquadMember, related_name='selected_for')
    starting = models.BooleanField(default=False)

    class Meta:
        unique_together = ('fixture', 'squad_member')

    def __str__(self):
        return str(self.squad_member)


class Goal(models.Model):
    scorer = models.ForeignKey('Selection', related_name='goals')
    assist = models.ForeignKey('Selection', null=True, related_name='assists')
    minute = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.minute:
            minute = " (%smin)" % self.minute
        else:
            minute = ""
        return "%s%s" % (self.scorer, minute)

    def date(self):
        return self.scorer.fixture.match_date()

    def opponent(self):
        return self.scorer.fixture.opponent


class Card(models.Model):
    YELLOW = 'yellow'
    RED = 'red'
    CARDS = (
        (YELLOW, YELLOW),
        (RED, RED)
    )
    color = models.CharField(max_length=8, choices=CARDS)
    recipient = models.ForeignKey('Selection')
    minute = models.IntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.minute:
            minute = " %smin" % self.minute
        else:
            minute = ""
        return "%s %s%s" % (self.color.upper(), self.recipient, minute)

    def date(self):
        return self.recipient.fixture.match_date()

    def opponent(self):
        return self.recipient.fixture.opponent
