from rest_framework.serializers import ModelSerializer
from .models import Grocery

class GrocerySerializer(ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'