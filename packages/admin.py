from django.contrib import admin
from . models import Packages, Offer

class PackagesAdmin(admin.ModelAdmin):
    list_display = ("name","price")
class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")

admin.site.register(Packages, PackagesAdmin)

admin.site.register(Offer, OfferAdmin)