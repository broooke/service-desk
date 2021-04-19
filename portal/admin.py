from django.contrib import admin
from portal.models import Application, ServiceDetail, Service

admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Application)
