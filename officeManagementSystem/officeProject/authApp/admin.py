from django.contrib import admin
from .models import *

admin.site.register(customUserModel)
admin.site.register(departmentModel)
admin.site.register(employerProfileModel)