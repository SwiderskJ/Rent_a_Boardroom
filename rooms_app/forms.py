from django import forms
from rooms_app.models import Room


class CreateRoomForm(forms.Form):
    name = forms.CharField(label='name')
    description = forms.CharField(label='description', widget=forms.Textarea)
    city = forms.CharField(label='city')
    street = forms.CharField(label='street')
    street_number = forms.CharField(label='street_number')
    local_number = forms.IntegerField(label='local_number')
    post_code_first = forms.IntegerField(label='post_code_first')
    post_code_second = forms.IntegerField(label='post_code_second')
    level = forms.IntegerField(label='level')
    capacity = forms.IntegerField(label='capacity')
    projector = forms.BooleanField(label='projector', required=False)
    seats = forms.IntegerField(label='seats')
    tables = forms.BooleanField(label='tables', required=False)
    catering = forms.BooleanField(label='catering', required=False)
    private_parking = forms.BooleanField(label='private_parking', required=False)
    sound_system = forms.BooleanField(label='sound_system', required=False)
