from .views import ProfileViewSet
from django.urls import path


urlpatterns = [
    path('<int:pk>/', ProfileViewSet.as_view()),
]
