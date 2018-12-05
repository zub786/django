from django import forms
import re

def validate_comment_word_count(value):
      count = len(value.split())
      if count < 3:
            raise forms.ValidationError(('''Please provide at least a 30 word message, %(count)s words is not descriptive enough'''), params={'count': count},)