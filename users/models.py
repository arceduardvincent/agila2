import uuid
import os


from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.dispatch import receiver

from generic.models import BaseModel
from model_utils import Choices


ADMIN_ROLE = 1
STAFF_ROLE = 2
CUSTOMER_ROLE = 3
CONTENT_CREATOR_ROLE = 4


def image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('', filename)

class Role(BaseModel):
    name = models.CharField(_('Role Name'), max_length=32)
    description = models.CharField(
        _('Description'),
        max_length=512, blank=True
    )

    def __str__(self):
        return self.name


class Profile(BaseModel):
    GENDER_CHOICES = Choices('Male', 'Female')
    image = models.ImageField(_('Profile Image'),
                              upload_to=image_file_path,
                              blank=True,
                              null=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name=_('User')
                                )
    role = models.ForeignKey('users.Role',
                             on_delete=models.CASCADE,
                             default=CUSTOMER_ROLE,
                             verbose_name=_('Role'))
    birth_date = models.DateField(_('Birth Date'),
                                  blank=True,
                                  null=True)
    address = models.TextField(_('Address'),
                               blank=True,
                               null=True)
    phone = models.CharField(_('Phone Number'),
                             max_length=50,
                             blank=True,
                             null=True)
    gender = models.CharField(_('Gender'),
                              max_length=50,
                              choices=GENDER_CHOICES,
                              default='')
    is_active = models.BooleanField(
        _('Is Active'),
        default=True)

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return self.user.get_full_name()

    def get_role_name(self):
        return "{}".format(self.role.name)

    @cached_property
    def is_admin(self):
        return self.role_id == ADMIN_ROLE


    @cached_property
    def is_customer(self):
        return self.role_id == CUSTOMER_ROLE


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
