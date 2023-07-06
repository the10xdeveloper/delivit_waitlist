from django.contrib import admin

# Register your models here.
from waitlist.models import UserData, UserDetail

admin.site.register(UserData)
admin.site.register(UserDetail)
