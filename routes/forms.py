from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label="City of departure", queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': ' form-control js-example-basic-single'}))

    to_city = forms.ModelChoiceField(
        label="City of destination", queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': ' form-control js-example-basic-single'}))

    traveling_time = forms.IntegerField(
        label="Traveling time",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in a trip'})
    )

    cities = forms.ModelMultipleChoiceField(label="Cities to visit", queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'form-control js-example-basic-multiple ', }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label="Route name", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ' Route name',
        }))

    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.HiddenInput()
    )

    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.HiddenInput()
    )

    overall_travel_time = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(), required=False,
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'form-control d-none', }))

    class Meta:
        model = Route
        fields = '__all__'

