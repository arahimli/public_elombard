from django.contrib import admin

# Register your models here.
from panel.models import *

class PackageAdmin(admin.ModelAdmin):
    list_display = ('customer','status',)
    list_max_show_all = 500
    list_per_page = 200

admin.site.register(Package,PackageAdmin)


admin.site.register(Customer)
admin.site.register(CustomerNote)
admin.site.register(WaitingPackage)
class PackagePaymentDatesAdmin(admin.ModelAdmin):
    list_display = ('package','month_count','date',)
    search_fields = ('package',)
    list_filter = ('package',)
    list_max_show_all = 500
    list_per_page = 200

admin.site.register(PackagePaymentDates,PackagePaymentDatesAdmin)

admin.site.register(PackageStatus)
admin.site.register(PackageOrder)
admin.site.register(Currency)
admin.site.register(PackageType)
admin.site.register(Department)
admin.site.register(Log)
admin.site.register(OutcomeType)
admin.site.register(OutcomeName)
admin.site.register(OutcomeType2)
admin.site.register(PackageProduct)
admin.site.register(PackageProductImage)
admin.site.register(IncomeOutcome)
admin.site.register(CustomerPhoneNumber)
admin.site.register(PackageDailyNote)