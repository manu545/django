from django.contrib import admin
from usrprofil.models import Profile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "roll", "phone", "address", "pin", "city", "parent_name", "parent_phone", "birthdate")
    search_fields = ["user__username", "roll", "phone", "address", "pin", "city", "parent_name", "parent_phone", "birthdate"]


admin.site.register(Profile, UserProfileAdmin)
