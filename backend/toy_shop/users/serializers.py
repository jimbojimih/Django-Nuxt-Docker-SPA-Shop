from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from cart.serializers import CartItemSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['city', 'street', 'house', 'number_phone', 'comments']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False) 
    
    class Meta:
        model = User
        fields = ['first_name', 'email', 'profile']
    
    def update(self, instance, validated_data):
        #user
        instance.first_name = validated_data.get(
                'first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        #profile        
        profile_data = validated_data.pop('profile', None)   
        if not profile_data:
            return instance   

        profile = instance.profile
        
        profile.city = profile_data.get('city', profile.city)
        profile.street = profile_data.get('street', profile.street)
        profile.house = profile_data.get('house', profile.house)
        profile.number_phone = profile_data.get(
                'number_phone', profile.number_phone)
        profile.comments = profile_data.get('comments', profile.comments)

        profile.save()
        return instance
    
