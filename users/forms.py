from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'contact_number', 'date_of_birth', 'address', 'bio', 'profile_picture']
        # Add fields you want to include in the form