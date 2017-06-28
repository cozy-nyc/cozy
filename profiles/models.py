from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# import stripe
# stripe.api_key = settings.STRIPE_SECERT_KEY

class Profile(models.Model):
    """
        This is a model extends the user model and provides details on user that are displayed publicly.

        Attributes:
            username: A string of the username tied to the profile
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    location = models.CharField(
        max_length = 40,
        default=''
    )
    bio = models.TextField(default='')
    rating = models.FloatField(
        default = 3.0,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
    )
    is_business = models.BooleanField(default=False)


# class UserStripe(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     stripe_id = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         if self.stripe_id:
#             return str(self.stripe_id)
#         else:
#             return self.user.username

# def stripeCallback(sender, request, user, **kwargs):
#     user_stripe_account, created = UserStripe.objects.get_or_create(user=user)
#     if created:
#         print('created for%s' %(user.username))
#     if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email=user.email)
#         user_stripe_account.stripe_id = new_stripe_id['id']
#         user_stripe_account.save()
#

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def updateUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
