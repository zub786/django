from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from cofeehouse.forms import ContactForm
from django.conf import settings
from cofeehouse.stores.models import Store
from django.contrib import messages
from django.http import HttpResponse
import json
from django.core import serializers
from rest_framework import serializers
from cofeehouse.stores.models import Store
# from cofeehouse.stores.serializers import StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def save_uploaded_file_to_media_root(f):
    with open('%s%s' % (settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST, request.FILES)
        # check if it's valid:
        if form.is_valid():
            # emailAddress = form.cleaned_data['email']
            # process data, insert into DB, generate email,etc
            # redirect to a new url:

            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    save_uploaded_file_to_media_root(formfile)
            # Create a model Store instance
            store_corporate = Store(name=form.cleaned_data['name'], address=form.cleaned_data['address'],
                                    city=form.cleaned_data['city'], state=form.cleaned_data['state'],
                                    email=form.cleaned_data['email'], comment=form.cleaned_data['comment'])

            # Invoke the save() method to create/save the record
            # No record id reference, so a create operation is made and the reference is updated with id
            store_corporate.save()

            # Invoke the save() method to update/save the record
            # Record has id reference from prior save() call, so operation is update
            store_corporate.save()
            return HttpResponseRedirect('/contact/contactconfirmation')
        else:
            pass

    else:
        # GET, generate blank form
        request.user.first_name = "zubair"
        request.user.email = "mzubairshakoor@hotmail.com"
        form = ContactForm(initial={'user': request.user, 'otherstuff': 'other stuff'})
    return render(request, 'contactus/contactus.html', {'form': form})


def contactconfirmation(request):
    return render(request, 'contactus/contactconfirmation.html')


def contacstindex(request):
    contacts = Store.objects.all()
    return render(request, 'contactus/contactindex.html', {'contacts': contacts})


def edit(request, id):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contacttoedit = Store.objects.get(id=id)
            contacttoedit.name = form.cleaned_data['name']
            contacttoedit.address = form.cleaned_data['address']
            contacttoedit.city = form.cleaned_data['city']
            contacttoedit.state = form.cleaned_data['state']
            contacttoedit.comment = form.cleaned_data['comment']
            contacttoedit.save()
            messages.add_message(request, messages.SUCCESS, 'Contact has updated successfully.')
            # return HttpResponseRedirect('/contact/contactconfirmation')
            return render(request, 'contactus/contactedit.html', {'form': form})
        else:
            pass
            return render(request, 'contactus/contactedit.html', {'form': form})

    else:
        contacttoedit = Store.objects.get(id=id)
        form = ContactForm(initial={'name': contacttoedit.name, 'state': contacttoedit.state,
                                    'email': contacttoedit.email,
                                    'city': contacttoedit.city, 'address': contacttoedit.address,
                                    'comment': contacttoedit.comment})
        return render(request, 'contactus/contactedit.html', {'form': form})


def delete(request, id):
    Store.objects.get(id=id).delete()
    messages.add_message(request, messages.SUCCESS, 'Contact has deleted successfully.')
    return redirect('/contact/index')


def rest_contacts(request):
    contact_list = Store.objects.all()
    for store in contact_list:
        print(store)
    # print(contact_list[0])
    # store_names = [{"contact": store.name} for store in contact_list]
    # return HttpResponse(json.dumps(store_names), content_type='application/json')
    serialized_stores = serializers.serialize('json', contact_list)
    return HttpResponse(serialized_stores, content_type='application/json')


@api_view(['GET'])
def rest_contacts_fw(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     ... #logic for HTTP POST  operation
    # elif request.method == 'DELETE':
    #     ... #logic for HTTP DELETE operation


class StoreSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(max_length=200)
    # email = serializers.EmailField()
    class Meta:
        model = Store
        fields = '__all__'
