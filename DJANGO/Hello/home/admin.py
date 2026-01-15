from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from home.models import Contact
from django.contrib.auth.models import User

# Admin branding
admin.site.site_header = "AVRA Admin"
admin.site.site_title = "Raj Admin Portal"
admin.site.index_title = "Welcome to Your AVRA VOID Portal"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "short_desc", "date")
    search_fields = ("name", "email", "phone")
    list_filter = ("date",)
    ordering = ("-date",)

    def short_desc(self, obj):
        return (obj.desc[:40] + "...") if obj.desc else ""

    short_desc.short_description = "Message"


class UserAdmin(admin.ModelAdmin):
    list_display=("username","email",'is_staff','is_active','last_login','date_joined')
    search_fields=("username","email")
    list_filter=('is_staff','is_active')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
