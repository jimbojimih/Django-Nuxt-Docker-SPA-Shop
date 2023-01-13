from django.urls import path, include
from .views import UserView


urlpatterns = [
    path('drf_auth/', include('rest_framework.urls')),
    path('', UserView.as_view()),
]