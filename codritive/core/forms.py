from django import forms
from .models import Contact
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number (+374XXXXXXXX)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "What's this about?"
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your project...'
            }),
        }

    def clean_phone_number(self):
        """Normalize common phone formats to +374XXXXXXXX and validate.

        Accepts inputs like:
        - +37412345678
        - 37412345678
        - 012345678 (local leading 0)
        - 12345678 (just 8 digits)
        """
        phone = self.cleaned_data.get('phone_number', '') or ''
        phone = phone.strip()

        # remove common separators/spaces/parentheses
        normalized = re.sub(r"[\s\-()]+", "", phone)

        # If it starts with 0 and length 9 (0 + 8 digits) -> replace 0 with +374
        if normalized.startswith('0') and len(normalized) == 9:
            normalized = '+374' + normalized[1:]
        # If it starts with '374' without + -> add +
        elif normalized.startswith('374') and not normalized.startswith('+'):
            normalized = '+' + normalized
        # If it's exactly 8 digits -> assume local number and prepend +374
        elif normalized.isdigit() and len(normalized) == 8:
            normalized = '+374' + normalized

        validator = RegexValidator(r'^\+374\d{8}$', 'Enter a valid Armenian phone number starting with +374 and followed by 8 digits.')
        try:
            validator(normalized)
        except ValidationError as e:
            raise forms.ValidationError(e.message)

        return normalized
