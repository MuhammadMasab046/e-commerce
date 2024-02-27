from .models import User 
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('first_name','last_name','email','password', 'phone_no', 'image')
        labels = {
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'Email',
            'password': 'Password',
            'phone_no': 'Phone No',
            'image': 'Image'
        }
        # def __init__(self, *args, **kwargs):
        #     super(UserForm, self).__init__(*args, **kwargs)

        # # Add Bootstrap classes to form fields
        #     for field_name in self.fields:
        #         self.fields[field_name].widget.attrs['class'] = 'form-control'

        # # Additional styling to place each field on a new line
        #     for field_name in ('first_name', 'last_name', 'email', 'password', 'phone_no', 'image'):
        #         self.fields[field_name].widget.attrs['class'] += ' form-row'