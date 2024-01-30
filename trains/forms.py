from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label="Train number",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter train number'}))

    travel_time = forms.CharField(label="Travel time",
                                  widget=forms.NumberInput(
                                      attrs={'class': 'form-control', 'placeholder': 'Enter travel time'}))

    from_city = forms.ModelChoiceField(label="City of departure", queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}
    ))

    to_city = forms.ModelChoiceField(label="City of arrival", queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single', }
    ))

    class Meta:
        model = Train
        fields = '__all__'
