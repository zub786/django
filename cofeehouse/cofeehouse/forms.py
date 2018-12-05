# # forms.py in app named 'contact'
# from django import forms
# from .formValidators import validate_comment_word_count
#
#
# class ContactForm(forms.Form):
#       name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
#       email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class': 'form-control'}))
#       comment = forms.CharField(widget=forms.Textarea, validators=[validate_comment_word_count])
#       city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#       state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#       address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#       error_css_class = 'error'
#       required_css_class = 'bold'
#       video = forms.FileField(required=False)
#       photo = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#
# def __init__(self, *args, **kwargs):
#             initial_arguments = kwargs.get('initial', None)
#             updated_arguments = {}
#             if initial_arguments:
#                 updated_arguments['name'] = getattr(initial_arguments, 'name', None)
#                 updated_arguments['state'] = getattr(initial_arguments, 'state', None)
#                 updated_arguments['email'] = getattr(initial_arguments, 'email', None)
#                 updated_arguments['address'] = getattr(initial_arguments, 'address', None)
#                 updated_arguments['city'] = getattr(initial_arguments, 'city', None)
#                 updated_arguments['comment'] = getattr(initial_arguments, 'comment', None)
#             kwargs.update(initial=updated_arguments)
#             super(ContactForm, self).__init__(*args, **kwargs)
#
#

from cofeehouse.stores.models import Store
from django import forms
from django.db import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        # widgets = {
        #     'name': models.CharField(max_length=25),
        #     'comment': forms.Textarea(attrs={'cols': 100, 'rows': 40})
        # }
        # labels = {
        #     'name': 'Full name',
        #     'comment': 'Issue'
        # }
        # help_texts = {
        #     'comment': 'Provide a detailed account of the issue to receive a quick answer'
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': "Name can only be 25 characters in length"
        #     }
        # }
        # field_classes = {
        #                     'email': EmailCoffeehouseFormField
        #                 },
        localized_fields = '__all__'