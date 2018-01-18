from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "country_id", "sex","is_customer")
    #list_display_links = ('name', 'code')
    #list_filter = ('name', 'code','indicatif','is_active')

    class Meta:
        model = User
admin.site.register(User, UserAdmin)