from django.contrib import admin

from .models import (Corporation, Coupon, CouponCorporate, CouponIndividual,
                     CustomerCorporate, CustomerIndividual, Payment)

# Register your models here.
admin.site.register(Corporation)
admin.site.register(CustomerIndividual)
admin.site.register(CustomerCorporate)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(CouponIndividual)
admin.site.register(CouponCorporate)
