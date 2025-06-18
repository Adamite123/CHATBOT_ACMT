from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')

    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your phone number.')
    address = forms.CharField(max_length=255, required=True, help_text='Required. Enter your address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email", "phone_number", "address", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COMMON_INPUT_CLASSES = 'w-full p-3 rounded-lg bg-black border border-[#44F3CA] placeholder-[#BFBFBF] focus:outline-none focus:ring-2 focus:ring-[#44F3CA]'

        self.fields['first_name'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Nama Depan'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Nama Belakang'
        })
        self.fields['email'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Email'
        })

        self.fields['phone_number'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Nomor Telepon'
        })
        self.fields['address'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Alamat Lengkap'
        })

        self.fields['username'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Kata Sandi',
            'type': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': COMMON_INPUT_CLASSES,
            'placeholder': 'Konfirmasi Kata Sandi',
            'type': 'password'
        })

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )

        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-lg bg-black border border-[#44F3CA] placeholder-[#BFBFBF] focus:outline-none focus:ring-2 focus:ring-[#44F3CA]',
            'placeholder': 'Masukkan Korporat/Pribadi'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 rounded-lg bg-black border border-[#44F3CA] placeholder-[#BFBFBF] focus:outline-none focus:ring-2 focus:ring-[#44F3CA]',
            'placeholder': 'Masukkan Kata Sandi'
        })
    )