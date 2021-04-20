from django.contrib import admin
from portal.models import Application, ServiceDetail, Service, Message

admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Application)
admin.site.register(Message)
