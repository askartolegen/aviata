from django.urls import path, include

from .views import *
urlpatterns = [
    path('', ),
    path('search/provider_a/', ProviderAView.as_view()),
    path('search/provider_b/', ProviderBView.as_view()),
    path('search/airflow/', AirflowView.as_view()),
    path('results/<str:search_id>/<str:currency>', AirflowView.as_view()),
]
