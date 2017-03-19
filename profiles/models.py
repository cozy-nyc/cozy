from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class profile(models.Model):
    name = models.CharField(max_length = 20)
    location = models.CharField(
        max_length = 40,
        default=''
    )
    bio = models.TextField(null = True)
    rating = models.FloatField(
        default = 3.0,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
    )
    verifiedStore = models.BooleanField (default = False)
    if( verifiedStore ):
        storeName = models.CharField(
            max_length = 20,
            default = '',
            blank = True
        )
    #Item/list

    def __str__(self):
        return self.name
