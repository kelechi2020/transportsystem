from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Reservation, Seat, Customer, Bus, Route, SeatChart
# Register your models here.
admin.site.site_header = 'Transport System Automation For Gombe Line Transport Services'
admin.site.site_title = 'Transport System Automation For Gombe Line Transport Services'


@admin.register(Reservation)
class ApplicantAdmin(ImportExportModelAdmin):
    pass
@admin.register(Route)
class ApplicantAdmin(ImportExportModelAdmin):
    pass
@admin.register(Bus)
class ApplicantAdmin(ImportExportModelAdmin):
    pass
@admin.register(Seat)
class ApplicantAdmin(ImportExportModelAdmin):
    pass
@admin.register(Customer)
class ApplicantAdmin(ImportExportModelAdmin):
    pass


admin.site.register(SeatChart)
