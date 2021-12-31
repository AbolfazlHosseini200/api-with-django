from rest_framework import serializers
from rest_framework import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'number')

    fields = '__all__'
