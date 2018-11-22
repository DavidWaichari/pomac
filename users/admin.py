from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','first_name','last_name', 'username','residence','profession','contact' ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'POMAC PETITION MASTER ADMINISTRATION'
admin.site.index_title = 'Pomac'
admin.site.site_title = 'System Administration'
