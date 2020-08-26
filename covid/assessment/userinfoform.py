from django import forms



sex = ('Male', 'Female')

class UserInfo(forms.Form):

    users_name = forms.CharField(label="Name" ,max_length=255)
    users_age = forms.CharField( label="Age", max_length=255 )
    #users_sex = forms.ChoiceField(choices=sex)
    users_temp = forms.CharField( label="Temperature", max_length=255 )