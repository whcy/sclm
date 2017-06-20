# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils.html import escape


class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'
    readonly_fields = ('content_type', 'user', 'action_time')
    actions = None

    list_filter = [
        # 'user',
        'content_type',
        'action_flag'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    """
    # Override Django's admin.ModelAdmin  
       get_list_display_links    method to remove links of list display of action_time
    """
    def get_list_display_links(self, request, list_display):

        if self.list_display_links or not list_display:
            return self.list_display_links
        else:
            return

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        return escape(obj.object_repr)

    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'内容摘要'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request).prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)
