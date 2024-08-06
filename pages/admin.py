from django.contrib import admin

# Register your models here.
from pages.models import UserForm
from pages.models import AdminForm
from pages.models import JobForm

admin.site.register(UserForm)
admin.site.register(AdminForm)
admin.site.register(JobForm)
admin.site.site_header = 'Monster'
admin.site.site_title = 'Monster'