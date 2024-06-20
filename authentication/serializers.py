from rest_framework import serializers
from .models import UserData


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 60, min_length = 8, write_only = True)

    class Meta:
        model = UserData
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')
    
        # check if username is alphanumeric
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric characters')

        
        return attrs 
    
    def create(self, validated_data):
        return UserData.objects.create_user(**validated_data)