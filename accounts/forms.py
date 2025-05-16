from.models import Profile
from django import forms
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class UpdateProfileForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo', 'contact', 'location')