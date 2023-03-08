from django import forms
from rooms_app.models import Room


class CreateRoomForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    city = forms.CharField()
    street = forms.CharField()
    street_number = forms.CharField()
    local_number = forms.IntegerField()
    post_code_first = forms.IntegerField()
    post_code_second = forms.IntegerField()
    level = forms.IntegerField()
    capacity = forms.IntegerField()
    projector = forms.BooleanField()
    seats = forms.IntegerField()
    tables = forms.BooleanField()
    catering = forms.BooleanField()
    private_parking = forms.BooleanField()
    sound_system = forms.BooleanField()
