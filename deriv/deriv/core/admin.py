from django.contrib import admin
from .models import Credential

# Register your models here.
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

#admin.site.register(Credentials)
admin.site.register(Credential, CredentialAdmin)
