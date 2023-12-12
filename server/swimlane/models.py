from django.core.validators import MaxValueValidator, URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from users_management.models import User


class PaymentChoice(models.TextChoices):
    CREDIT = "C", _("CREDIT")
    DEBIT = "D", _("DEBIT")
    GIFT = "G", _("GIFT")


class CouponChoice(models.TextChoices):
    INDIVIDUAL = "I", _("INDIVIDUAL")
    CORPORATE = "C", _("CORPORATE")


class Corporation(models.Model):

    corp_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    registration_number = models.CharField(max_length=100, null=False, blank=False)
    domain = models.CharField(max_length=100, null=False, blank=False, validators=[URLValidator])

    class Meta:
        indexes = [
            models.Index(fields=['domain']),
        ]

    def __str__(self):
        return self.name


class CustomerIndividual(models.Model):
    customer_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='individual_customer')
    dl_number = models.CharField(max_length=100, null=False, blank=False)
    insurance_company = models.CharField(max_length=100, null=False, blank=False)
    insurance_policy_no = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.customer_id.email


class CustomerCorporate(models.Model):
    customer_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='corporate_customer')
    corp_id = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.customer_id.email


class Payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=1, null=False, blank=False, choices=PaymentChoice.choices)
    card_number = models.CharField(max_length=100, null=False, blank=False)
    # for gift card we make this false
    is_valid = models.BooleanField(default=True)
    card_name = models.CharField(max_length=100, null=False, blank=False)
    card_exp_date = models.DateField(null=False, blank=False)
    card_zipcode = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        return f"{PaymentChoice(self.payment_method).name.lower()} card of {self.customer_id.email}"


class Coupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    coupon_code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    coupon_type = models.CharField(null=False, blank=False, max_length=1, choices=CouponChoice.choices)
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MaxValueValidator(100)]
    )
    is_valid = models.BooleanField(null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['coupon_code']),
            models.Index(fields=['coupon_id', 'coupon_code']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(coupon_type__in=[i[0] for i in CouponChoice.choices]),
                name='ch_inh_dsr_coupon'
            )
        ]

    def __str__(self):
        return f"[{self.coupon_id}] {CouponChoice(self.coupon_type).name.lower()} coupon with discount {self.discount}"


class CouponIndividual(models.Model):
    coupon_id = models.OneToOneField(Coupon, primary_key=True, on_delete=models.CASCADE, related_name='individual_coupon')
    valid_from = models.DateField(null=False, blank=False)
    valid_to = models.DateField(null=False, blank=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(valid_to__gte=models.F('valid_from')), name='dsr_coupon_indiv_chk_date'),
        ]

    def __str__(self):
        return f"[{self.coupon_id}] {self.valid_from} {self.valid_to}"


class CouponCorporate(models.Model):
    coupon_id = models.OneToOneField(Coupon, primary_key=True, on_delete=models.CASCADE, related_name='corporate_coupon')
    corp_id = models.ForeignKey(Corporation, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.coupon_id}] {self.corp_id.name}"
