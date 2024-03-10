from django.contrib import admin
from .models import Domain,DomainTenantAwareModel

admin.site.register(Domain)
admin.site.register(DomainTenantAwareModel)