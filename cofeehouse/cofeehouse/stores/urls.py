from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.stores, name='store'),
    url(r'^goods/$', views.goodsStore, name='goodsStore'),
    url(r'^(?P<store_id>)[0-9]+$', views.storeDetail, name='storeDetails'),


]
