from django.db import models

class SiteSetting(models.Model):
    company_name = models.CharField(max_length=255, default="WIDE Range Logistics LLC", verbose_name="Business Name")
    tagline = models.CharField(max_length=255, default="Reliable Logistics Solutions", blank=True, verbose_name="Tagline / Subtitle")
    phone = models.CharField(max_length=50, default="(216) 677-1799", verbose_name="Phone Number")
    email = models.EmailField(default="chris@northernstarlogisticsinc.com", verbose_name="Contact Email")
    address = models.CharField(max_length=255, default="419 Interlude Rd, New Iberia, LA 70563, USA", blank=True, verbose_name="Physical Address")
    working_hours = models.CharField(max_length=100, default="24/7 Our Support", blank=True, verbose_name="Support / Working Hours")
    copyright_text = models.CharField(max_length=255, default="© 2026 WIDE Range Logistics LLC. All rights reserved.", blank=True, verbose_name="Footer Copyright Text")
    
    # Logos
    logo = models.ImageField(upload_to="settings/", blank=True, null=True, verbose_name="Main Logo (Navbar)", help_text="Upload custom logo to replace default logo")
    white_logo = models.ImageField(upload_to="settings/", blank=True, null=True, verbose_name="White / Header Strip Logo", help_text="Upload logo for dark backgrounds or top strip")
    
    # Agreement Specific Details
    usdot_number = models.CharField(max_length=50, default="#2248522", blank=True, verbose_name="Broker USDOT")
    mc_number = models.CharField(max_length=50, default="#741715", blank=True, verbose_name="Broker MC")
    broker_signer_name = models.CharField(max_length=100, default="Chris Mitchell", blank=True, verbose_name="Broker Signer Name")
    broker_signature = models.ImageField(upload_to="settings/", blank=True, null=True, verbose_name="Broker Signature Image")
    deposit_fee = models.CharField(max_length=50, default="$399", blank=True, verbose_name="Deposit / Slot Fee")
    
    # Social links
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook URL")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn URL")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram URL")

    class Meta:
        verbose_name = "Store & Business Settings"
        verbose_name_plural = "Store & Business Settings"

    def __str__(self):
        return f"{self.company_name} Settings"

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


class CarrierAgreement(models.Model):
    # Carrier Info
    carrier_name = models.CharField(max_length=255)
    carrier_usdot_number = models.CharField(max_length=50, blank=True, null=True)
    carrier_usdot_mc = models.CharField(max_length=50, blank=True, null=True)
    carrier_phone = models.CharField(max_length=20, blank=True, null=True)
    agreement_date = models.DateField()

    # Banking Info
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)

    # Signatory Info
    signer_full_name = models.CharField(max_length=255, blank=True, null=True)
    signer_title = models.CharField(max_length=255, blank=True, null=True)
    signer_email = models.EmailField(blank=True, null=True)
    signature_text = models.CharField(max_length=1024, blank=True, null=True)

    # Deposit Method
    deposit_method = models.CharField(max_length=100, blank=True, null=True)

    # Terms & Metadata
    accepted_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.carrier_name} ({self.carrier_usdot_mc or 'N/A'})"
