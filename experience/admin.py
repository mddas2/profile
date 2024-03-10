from django.contrib import admin
from .models import ProfessionCategory,Experience,Skills
# Register your models here.
admin.site.register([ProfessionCategory,Experience,Skills])
