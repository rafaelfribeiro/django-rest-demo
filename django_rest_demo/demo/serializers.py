from rest_framework import serializers
from .models import ClientUser

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = '__all__'