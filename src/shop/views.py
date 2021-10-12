from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime
import os

class ShopView(APIView):
    def get(self, request):
        file_name = f'{datetime.now().strftime("%Y-%m-%d")}-shop-info.csv'
        file_path = f'{settings.MEDIA_ROOT}/{file_name}'
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                response = HttpResponse(file, content_type = 'text/csv')
                response['Content-Disposition'] = f'attachment; filename={file_name}'
                return response
        return Response(data = 'No shop report today', status = status.HTTP_200_OK)