from django import forms
from myproject.myapp.features.gaming.game.model.GamingModel import GamingModel as mModel


# Book Form
class GamingCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'
