from django.contrib import admin
from .models import ChaiVriety, ChaiCertificate, Reviews, Store

# Register your models here.
class ChaiReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_add')  # Corrected 'date_added' to 'date_add'
    inlines = [ChaiReviewInLine]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variety',)  # Uncommented and corrected to match the model field

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(ChaiVriety, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
