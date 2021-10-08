from django.urls import path

from order.views import (OrderView, OrderDeleteView)

urlpatterns = [
    path('', OrderView.as_view(), name = 'order get, post'),
    path('<int:pk>/', OrderDeleteView.as_view(), name = 'order delete')
]
