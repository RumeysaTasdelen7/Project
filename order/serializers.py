from rest_framework import serializers
from .models import Address, Product, Order

class OrderSerializer(serializers.ModelSerializer):

    address = serializers.CharField(allow_blank=True)
    product = serializers.CharField(allow_blank=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'quantity', 'price', 'status', 'address', 'product', 'created_at', 'updated_at']

    def validate(self, attrs):
        if 'address' in attrs:
            try:
                address = Address.objects.get(pk=attrs['address'])
            except Address.DoesNotExist:
                raise serializers.ValidationError({'address': 'Invalid pk "{}" - object does not exist.'.format(attrs['address'])})

        if 'product' in attrs:
            try:
                product = Product.objects.get(pk=attrs['product'])
            except Product.DoesNotExist:
                raise serializers.ValidationError({'product': 'Invalid pk "{}" - object does not exist.'.format(attrs['product'])})

        return attrs

