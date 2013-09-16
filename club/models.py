from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    joined = models.ForeignKey('Season', related_name='new_players')
    last_season = models.ForeignKey('Season', blank=True, related_name='l+', null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class SquadMember(models.Model):
    season = models.ForeignKey('Season', related_name='squad')
    player = models.ForeignKey('Player')
    pence_owing = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player)


class Season(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Date(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)


class Profile(models.Model):
    squad_member = models.ForeignKey('SquadMember', related_name='profile')
    profile = models.TextField(blank=True)
    pic = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return self.squad_member.name


class ProfileQuestion(models.Model):
    question = models.CharField(max_length=255)
    season = models.ForeignKey('Season')

    def __str__(self):
        return self.question


class ProfileAnswer(models.Model):
    question = models.ForeignKey('ProfileQuestion')
    answer = models.CharField(max_length=255)
    profile = models.ForeignKey('Profile', related_name='answers')

    def __str__(self):
        return '%s: "%s"' % (self.profile.squad_member.name, self.answer)