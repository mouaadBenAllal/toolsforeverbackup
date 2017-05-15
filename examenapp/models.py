from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


# Model van fabriek.
class Fabriek(models.Model):
    fabrieksnaam = models.CharField(max_length=45)
    telefoonnummer = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{0,10}$')])

