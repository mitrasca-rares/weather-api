from django import urls
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'locations', views.LocationViewSet, basename='location')

urlpatterns = [
    urls.path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    urls.path('auth/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    urls.path('', include(router.urls)),
]