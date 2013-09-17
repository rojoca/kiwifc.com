from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import TabularInline
from fixtures.models import *


class SelectionInlineForm(ModelForm):
    pass


class SelectionInline(TabularInline):
    model = Selection
    sortable = 'id'
    verbose_name_plural = 'Lineup'
    list_filter = ('fixture__league__season',)
    extra = 11
    max_num = 16

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(SelectionInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'squad_member':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(season__exact=request._obj_.league.season)
            else:
                field.queryset = field.queryset.none()

        return field


class FixtureAdmin(admin.ModelAdmin):
    inlines = (SelectionInline,)
    search_fields = ['opponent__name']
    list_display = ('result', 'score', 'match_date', 'match_time', 'opponent', 'venue')
    list_display_links = ('match_date', 'match_time', 'opponent')
    list_filter = ('league', 'played', 'home_game')
    list_select_related = True

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(FixtureAdmin, self).get_form(request, obj, **kwargs)


class GoalAdmin(admin.ModelAdmin):
    list_display = ('scorer', 'date', 'opponent', 'minute', 'description')
    list_filter = ['scorer']


class CardAdmin(admin.ModelAdmin):
    list_display = ('color', 'recipient', 'date', 'opponent', 'minute', 'reason')


class OpponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'home_ground')


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('season', 'name')


admin.site.register(League, LeagueAdmin)
admin.site.register(Venue)
admin.site.register(Opponent, OpponentAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Card, CardAdmin)

