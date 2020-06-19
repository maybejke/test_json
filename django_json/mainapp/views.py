from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Order, Product


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/index.html', {})


class ImpExpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/import-export.html', {})


class IndustryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/import-export.html', {})


class ChartImportExportData(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        orders_import = Order.objects.filter(direction_of_travel__exact=2.0,
                                             type_of_goods_apk__parent_id__exact=1.0).count()
        orders_export = Order.objects.filter(direction_of_travel__exact=3.0,
                                             type_of_goods_apk__parent_id__exact=1.0).count()
        labels = ['import', 'export']
        default_items = [orders_import, orders_export]
        data = {
            'labels': labels,
            'default': default_items
        }
        return Response(data)


class ChartIndustryData(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = []
        industry = Product.objects.all().values('parent_id').distinct('parent_id')

        for el in industry:
            name = Product.objects.filter(parent_id__exact=industry['parent_id'])
            for n in name:
                labels.append(n.name)

        default_items = list(industry)
        data = {
            'labels': labels,
            'default': default_items
        }
        return Response(data)
