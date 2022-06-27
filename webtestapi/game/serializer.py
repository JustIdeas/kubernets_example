from rest_framework import serializers
from game.models import store
from django.contrib.auth.models import User
class gameSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        fields = ['id', 'name', 'category', 'description']

class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'

