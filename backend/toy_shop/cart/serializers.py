from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image_url = obj.item.images.first().image.url
        return self.context['request'].build_absolute_uri(image_url)

    class Meta:
        model = CartItem
        fields = '__all__'