from datetime import timedelta
from django.contrib import admin
from tracking.models import Visitor, Pageview
from tracking.settings import TRACK_PAGEVIEWS

class VisitorAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'

    list_display = ('session_key', 'user', 'start_time', 'session_over',
        'pretty_time_on_site', 'ip_address', 'user_agent', 'source', 'medium')
    list_filter = ('user', 'ip_address', 'source', 'medium')
    search_fields = ('session_key', 'user__username', 'user__email', 'user__first_name', 'user__last_name')

    def session_over(self, obj):
        return obj.session_ended() or obj.session_expired()
    session_over.boolean = True

    def pretty_time_on_site(self, obj):
        if obj.time_on_site is not None:
            return timedelta(seconds=obj.time_on_site)
    pretty_time_on_site.short_description = 'Time on site'


admin.site.register(Visitor, VisitorAdmin)


class PageviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'view_time'

    list_display = ('url', 'view_time', 'get_session_key', 'get_user')
    list_filter = ('visitor__user', )
    search_fields = ('visitor__session_key', 'visitor__user__username', 'visitor__user__email', 'visitor__user__first_name', 'visitor__user__last_name')

    def get_session_key(self, obj):
        return obj.visitor.session_key

    def get_user(self, obj):
        return obj.visitor.user

if TRACK_PAGEVIEWS:
    admin.site.register(Pageview, PageviewAdmin)
