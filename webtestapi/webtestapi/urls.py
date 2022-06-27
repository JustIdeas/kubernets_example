
from django.contrib import admin
from django.urls import path, include
from game.views import gameViewSet

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'store', gameViewSet)

urlpatterns = [
    path('api_auth/', obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
