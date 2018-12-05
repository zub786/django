from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^contactus/$', views.contact, name='contactus'),
    url(r'^contactconfirmation/$', views.contactconfirmation, name='contactconfirmation'),
    url(r'^index/$', views.contacstindex, name='contactindex'),
    url(r'^edit/(?P<id>\d)', views.edit, name='contactedit'),
    url(r'^delete/(?P<id>\d)', views.delete, name='contactdelete'),
    url(r'^rest_contacts/$', views.rest_contacts, name='restcontacts'),
    url(r'^rest_contacts_fw/$', views.rest_contacts_fw, name='restcontactsfw'),
    # url(r'^view/(?P<id>\d)', views.view, name='contactview'),

]
