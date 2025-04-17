from django import forms
from .models import *

class MessageModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','type':'email','id':'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text','id':'phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text','id':'phone', 'placeholder':'Leave a Message...'}))
    class Meta:
        model = MessageModel
        fields = ('name', 'email', 'phone', 'message')

class CourseModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','type':'email','id':'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text','id':'phone'}))
    # message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text','id':'phone', 'placeholder':'Leave a Message...'}))
    class Meta:
        model = CourseModel
        fields = ('name', 'email', 'phone', 'desired_course', 'mode_of_study')