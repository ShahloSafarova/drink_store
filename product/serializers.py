from rest_framework import serializers
from .models import Category, Ingredient, Drink, DrinkIngredient, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class DrinkIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkIngredient
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
