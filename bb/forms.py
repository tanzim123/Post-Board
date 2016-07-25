from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

class RegisterForm(forms.ModelForm):

	password = forms.CharField(label='Password',
		widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password',
		widget=forms.PasswordInput)

	class Meta:

		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Your password did not match.')
		return cd['password2']


class LoginForm(forms.Form):

        username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'usernameClass'}))
        password = forms.CharField(widget=forms.PasswordInput())


class createpost(ModelForm):

	name = forms.CharField()

	class Meta:
		model = Post
		fields = ['title','slug','body']


