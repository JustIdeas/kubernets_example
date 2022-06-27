from rest_framework import viewsets
from game.models import store
from game.serializer import gameSerializer
from .serializer import userSerializers
from django.contrib.auth.models import User

class gameViewSet(viewsets.ModelViewSet):
    queryset = store.objects.all()
    serializer_class = gameSerializer

class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers
