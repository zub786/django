from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


def stores(request):
    # Content from request or database extracted here
    # and passed to the template for display
    messages.success(request, "Welcome at your store")
    return render(request, 'stores/stores.html')


def goodsStore(request):
    # Content from request or database extracted here
    # and passed to the template for display
    return render(request, 'stores/goodsStore.djhtml')


def storeDetail(request, store_id=None):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    STORE_NAME = 'Downtown'
    store_address = {'street': 'Main #385', 'city': 'San Diego', 'state': 'CA', 'Store_Id': store_id}
    store_amenities = ['WiFi', 'A/C', ]
    store_menu = ((0, ''), (1, 'Drinks'), (2, 'Food'))
    values_for_template = {'store_name': STORE_NAME, 'store_address': store_address,
                           'store_amenities': store_amenities, 'store_menu': store_menu}
    return render(request, 'stores/detail.html', values_for_template)

