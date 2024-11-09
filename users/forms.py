from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name','email', 'contact_number', 'date_of_birth', 'address', 'bio', 'profile_picture']
        # Add fields you want to include in the form
        date_of_birth = forms.DateField(
            input_formats=['%Y-%m-%d'],  # specify the format
            widget=forms.DateInput(attrs={'type': 'date'})  # optional: use HTML5 date input field
        )