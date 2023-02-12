from django.urls import path
from .views import canceled, success, items, item, buy


urlpatterns = [
    path('', items, name='items'),
    path('canceled/', canceled, name='canceled'),
    path('success/', success, name='success'),
    path('item/<int:id>/', item, name='item'),
    path('buy/<int:id>/', buy, name='buy')
]