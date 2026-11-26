from django.contrib import admin
from .models import CarrierAgreement, SiteSetting

admin.site.site_header = "Logistics & Store Administration"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Business Management & Settings"

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🏢 Business Identity", {
            'fields': ('company_name', 'tagline', 'logo', 'white_logo'),
            'description': 'Customize your brand name and logos across the entire website.'
        }),
        ("📞 Contact Details", {
            'fields': ('phone', 'email', 'address', 'working_hours'),
            'description': 'These details will automatically update in headers, footers, contact pages, and agreements.'
        }),
        ("📄 Agreement & Broker Settings", {
            'fields': ('usdot_number', 'mc_number', 'broker_signer_name', 'broker_signature', 'deposit_fee'),
            'description': 'Settings used in generated PDF agreements and online broker forms.'
        }),
        ("🌐 Footer & Social Links", {
            'fields': ('copyright_text', 'facebook_url', 'linkedin_url', 'instagram_url')
        }),
    )

    def has_add_permission(self, request):
        # Disallow adding more than one settings object
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CarrierAgreement)
class CarrierAgreementAdmin(admin.ModelAdmin):
    list_display = ('carrier_name','carrier_usdot_mc','agreement_date','created_at')
    search_fields = ('carrier_name','carrier_usdot_mc','signer_full_name')
