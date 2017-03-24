from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
class MyAdminSite(AdminSite):
    site_header = 'TECH-X'
admin_site = MyAdminSite(name='myadmin')
class CustAdmin(admin.ModelAdmin):
    list_display= ["accountno","custname","balance"]
    search_fields = ["accountno","custname"]
    #list_filter=["connectionstatus"]
    class Meta:
        model=consumers
admin.site.register(consumers,CustAdmin)
admin_site.register(consumers,CustAdmin)
class PaymentAdmin(admin.ModelAdmin):
    list_display= ["connectionCode","payment","paydate"]
    search_fields = ["connectionCode","receiptno"]

    class Meta:
        model=payments
admin.site.register(payments,PaymentAdmin)
admin_site.register(payments,PaymentAdmin)

