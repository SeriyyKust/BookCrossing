from .views import ProfileViewSet
from django.urls import path

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'})),
    path('update/<int:pk>/', ProfileViewSet.as_view({'patch': 'update'})),
]
