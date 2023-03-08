from .views import ProfileViewSet, get_all_profiles
from django.urls import path


urlpatterns = [
    path('all/', get_all_profiles),
    path('<int:pk>/', ProfileViewSet.as_view()),
]
