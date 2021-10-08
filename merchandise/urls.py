from django.urls import path

from merchandise.views import (
    ProductView
)

urlpatterns = [
    path('', ProductView.as_view(), name = 'product'),
]
