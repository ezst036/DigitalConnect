from django.contrib import admin
from connect.models import ContactConnect

class DigitalConnectAdmin(admin.AdminSite):
    site_header = 'Digital Connect Administration'
    index_title = "Administration Portal"
    list_display = ('title', 'body')

    #fieldsets = ()

connectadmin = DigitalConnectAdmin(name='ConnectAdmin')

admin.site.register(ContactConnect)
connectadmin.register(ContactConnect)