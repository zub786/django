from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Store(models.Model):
    #id = models.AutoField(primary_key=True)# Added by default, not required explicitly
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=50, null=True)
    #objects = models.Manager()# Added by default, to required explicitly
    def __str__(self):
        return "%s (%s,%s)" % (self.name, self.city, self.state)