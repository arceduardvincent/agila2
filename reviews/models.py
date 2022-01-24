from django.db import models
from django.contrib.auth.models import User
from generic.models import BaseModel
from django.utils.translation import ugettext_lazy as _


RATING_CHOICES = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


class Review(BaseModel):
    rating = models.CharField(
        _("Rating"),
        max_length=50,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.rating

