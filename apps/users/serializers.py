from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear usuarios"""
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password_confirm', 'isPremiumUser']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    """Serializer para listar usuarios"""
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'isPremiumUser', 'date_joined', 'is_active']
