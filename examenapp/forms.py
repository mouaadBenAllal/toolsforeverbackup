from django.forms import ModelForm
from .models import Fabriek


# Form van model: Fabriek.
# Hierin wordt aangegeven welke model er gebruikt gaat worden en welke velden van de model.
class FabriekForm(ModelForm):
    class Meta:
        model = Fabriek
        fields = ['fabrieksnaam', 'telefoonnummer', ]

