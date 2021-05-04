from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['nombres'].widget.attrs['class'] = 'form-control'
        self.fields['apellidos'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    password1 = forms.CharField(
        label='Contraseña',
        required=True, 
        widget=forms.PasswordInput(
            attrs={'placeholder' : 'contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True, 
        widget=forms.PasswordInput(
            attrs={'placeholder' : 'Repetir Contraseña'
            }
        )
    )
    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
        )

     
    

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden') 

class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
   

    username = forms.CharField(
        label='username',
        required=True, 
        widget=forms.TextInput(
            attrs={'placeholder' : 'Username'}
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True, 
        widget=forms.PasswordInput(
            attrs={'placeholder' : 'Contraseña'}
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Por favor verifique los datos de usuario')    
        
        return self.cleaned_data