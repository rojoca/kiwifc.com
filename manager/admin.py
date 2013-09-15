from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from manager.models import *


class ManagerModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(MatchReport, ManagerModelAdmin)
admin.site.register(Prematch, ManagerModelAdmin)
admin.site.register(Fine, ManagerModelAdmin)
