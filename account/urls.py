from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, logout_view

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
# router.register(r'auth', AuthViewSet, basename='auth')

app_name = 'account'

urlpatterns = [
    path('', include(router.urls)),
    path('logout', logout_view, name='logout'),
]