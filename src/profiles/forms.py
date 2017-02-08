from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='100 charactot max')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget = forms.Textarea)


# class loginForm(forms.Form):
#     username = forms.CharField(required=True, max_length=30)
#     password = forms.CharField(required=True, max_length=10, min_length=8)
#
#
# class signupForm(forms.Form):
#     username = forms.CharField(required=True, max_length=30)
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, max_length=10, min_length=8)
#     confirm_password = forms.CharField(required=True, max_length=10, min_length=8)
