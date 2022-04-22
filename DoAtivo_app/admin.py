from django.contrib import admin
from models import Donor, Donation, Institute

class DonorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    search_fields = ["id", "name", "email"]
    list_filter = ["donations"]
    list_per_page = 10

class InstituteAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    search_fields = ["name", "email"]
    list_filter = ["donations"]
    list_per_page = 10

class DonationAdmin(admin.ModelAdmin):
    list_display = ["id", "food", "reciver"]
    search_fields = [ "food", "reciver"]
    list_filter = ["reciver"]
    list_per_page = 10


admin.site.register(Donor, DonorAdmin)
admin.site.register(Donation, DonationAdmin)
admin.sites.register(Institute, InstituteAdmin)
