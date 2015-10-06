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
