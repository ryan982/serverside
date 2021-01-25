from django import forms

class QueryForm(forms.Form):
    email = forms.CharField(label = 'Email address',max_length=100)
    subject = forms.CharField(label = 'Subject', max_length=200)
    detail = forms.CharField(label="Describe in detail", max_length=2000)
# from django import forms

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)