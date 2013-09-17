from django.contrib import admin
from club.models import *


class SquadInline(admin.TabularInline):
    model = SquadMember
    verbose_name_plural = 'Squad'
    extra = 0


class SeasonAdmin(admin.ModelAdmin):
    inlines = (SquadInline,)


class ProfileAnswerChoiceInline(admin.TabularInline):
    model = ProfileAnswerChoice
    verbose_name_plural = 'Restrict answers to the following'
    extra = 0


class ProfileQuestionAdmin(admin.ModelAdmin):
    inlines = [ProfileAnswerChoiceInline]
    list_filter = ['season']
    list_display = ('season', 'question')
    list_display_links = ['question']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_name', 'last_name', 'email', 'mobile')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'first_name', 'last_name', 'email')


admin.site.register(Season, SeasonAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Profile)
admin.site.register(ProfileQuestion, ProfileQuestionAdmin)