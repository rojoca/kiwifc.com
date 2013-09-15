from django.contrib import admin
from club.models import *


class SquadInline(admin.TabularInline):
    model = SquadMember
    verbose_name_plural = 'Squad'
    extra = 0


class SeasonAdmin(admin.ModelAdmin):
    inlines = (SquadInline,)


admin.site.register(Season, SeasonAdmin)
admin.site.register(Player)
