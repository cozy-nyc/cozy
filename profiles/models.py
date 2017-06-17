from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


import stripe
stripe.api_key = settings.STRIPE_SECERT_KEY

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    displayName = models.CharField(
        max_length=20,
        unique=True
        )
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
    #Item/list

    def __str__(self):
        return self.displayName

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
