from django.urls import path
from .views import HomeView, ChartImportExportData, ImpExpView, IndustryView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('import-export/', ImpExpView.as_view(), name='import-export'),
    path('industry/', IndustryView.as_view(), name='industry'),
    path('api/chart/data/', ChartImportExportData.as_view()),
    path('api/chart/data/industry/', ChartImportExportData.as_view()),
]
