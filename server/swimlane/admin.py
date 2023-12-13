from django.contrib import admin

from .models import (Corporation, Coupon, CouponCorporate, CouponIndividual,
                     CustomerCorporate, CustomerIndividual, Payment)


# Register your models here.
@admin.register(Corporation)
class CorporationAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Corporation._meta.fields]
    list_display = [field.name for field in Corporation._meta.fields]


@admin.register(CustomerIndividual)
class CustomerIndividualAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in CustomerIndividual._meta.fields]
    list_display = [field.name for field in CustomerIndividual._meta.fields]


@admin.register(CustomerCorporate)
class CustomerCorporateAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in CustomerCorporate._meta.fields]
    list_display = [field.name for field in CustomerCorporate._meta.fields]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Payment._meta.fields]
    list_display = [field.name for field in Payment._meta.fields]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Coupon._meta.fields]
    list_display = [field.name for field in Coupon._meta.fields]


@admin.register(CouponIndividual)
class CouponIndividualAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in CouponIndividual._meta.fields]
    list_display = [field.name for field in CouponIndividual._meta.fields]


@admin.register(CouponCorporate)
class CouponCorporateAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in CouponCorporate._meta.fields]
    list_display = [field.name for field in CouponCorporate._meta.fields]
