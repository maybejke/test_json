from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
        return render(request, 'mainapp/industry.html', {})


class ChartImportExportData(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = [label.name for label in Product.objects.filter(parent_id='1.0')]

        industry_count = []

        ind_id = [label.id for label in Product.objects.filter(parent_id='1.0')]
        for i in ind_id:
            num = Product.objects.filter(parent_id=i).count()
            industry_count.append(num)

        data = {
            'labels': labels,
            'default': industry_count
        }
        return Response(data)
