from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView,PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
