# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.contrib import admin
from .models import Character, Session, Campaign, Criteria


class SessionInline(admin.TabularInline):
    model = Session
    extra = 3


class CampaignAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    #inlines = [SessionInline]

admin.site.register(Character)
admin.site.register(Session)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Criteria)
