from django import forms
from .models import Discount


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['code', 'discount_type',
                  'amount', 'active', 'expiration_date']
    expiration_date = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Specify the input format
        widget=forms.DateInput(
            attrs={
                'type': 'text',  # Change to 'text' type
                'placeholder': 'DD/MM/YYYY'  # Add a placeholder for clarity
            }
        )
    )
