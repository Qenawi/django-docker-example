from django import forms
from myproject.myapp.features.gaming.game_match.model.MatchModule import MatchModel as mModel


# Book Form
class MatchCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'
