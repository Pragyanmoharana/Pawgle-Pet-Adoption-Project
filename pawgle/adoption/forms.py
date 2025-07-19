from django import forms
from .models import DonatePet
from .models import Pet

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import AdoptionRequest


class DonatePetForm(forms.ModelForm):
    class Meta:
        model = DonatePet
        fields = ['name', 'pet_type', 'breed', 'age', 'gender', 'description', 'image', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_type': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),  # ✅ Added gender widget
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'email', 'password1', 'password2']
  labels = {'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
  
  
    
class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))





class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['contact_number', 'address', 'reason', 'family_members', 'had_pets_before']
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'family_members': forms.NumberInput(attrs={'class': 'form-control'}),
            'had_pets_before': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
from django.contrib.auth import password_validation


class MyPasswordChangeForm(PasswordChangeForm):
 old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,  'class':'form-control'}))
 new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
 new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
 email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
 new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
 new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))
