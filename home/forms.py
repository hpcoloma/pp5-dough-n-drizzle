from django import forms
from .models import NewsletterSubscription


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    subject = forms.CharField(
        max_length=100,
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email
