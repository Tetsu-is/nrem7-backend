from django.urls import path, include
from myapp import views
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('api', views.ProductView.as_view(), name='api'),
    path('general', views.GeneralView.as_view(), name='api2'),
]
