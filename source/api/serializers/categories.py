from rest_framework import serializers
from shop.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category',)
        model = Category

    def to_representation(self, instance):
        return instance.category