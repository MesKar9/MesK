from django.contrib import admin
from home.models import Setting, ContactFormMessage, UserProfile

# Register your models here.

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = [
        'contact_firstName',
        'contact_lastName',
        'contact_email',
        'contact_subject'
        ]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user_name',
        'city',
        'phone'
    ]



admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)