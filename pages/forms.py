from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}),error_messages={'required': 'Please enter your username.'})
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), error_messages={'required': 'Please enter your password.'})
    option = forms.ChoiceField(choices=(('option1', 'User'), ('option2', 'Admin')), widget=forms.RadioSelect ,error_messages={'required': 'Please choose your rule.'})
    remember_me = forms.BooleanField(required=False, label='Remember Me')

class UserSignUp(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    mail = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    rePassword = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Retype-Password'}))
    talent = forms.ChoiceField(choices=(('Company Admin', 'Company Admin'), ('Job Seeker', 'Job Seeker'),('Recuiter','Recuiter'),('Freelancer','Freelancer')), widget=forms.RadioSelect)

class AdminSignUp(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    mail = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    rePassword = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Retype-Password'}))
    companyName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Company Name'}))

class Form(forms.Form):
    STATUS_CHOICES = (
        ('Opened', 'Opened'),
        ('Closed', 'Closed'),
    )
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)
    number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Job ID'}))
    salary=forms.CharField(max_length=20, widget=forms.NumberInput(attrs={'placeholder': 'Salary'}))
    title=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Job Title'}))
    companyName=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    description=forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'description'}))
