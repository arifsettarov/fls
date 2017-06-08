from django import forms
from .models import Workers,User_DATA
class Create_Order_form(forms.ModelForm):
    class Meta:

        fields = '__all__'



class Register_Form(forms.ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'

