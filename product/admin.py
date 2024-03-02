from django.contrib import admin
from .models import Category, Ingredient, Drink, DrinkIngredient, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Ingredient, IngredientAdmin)

class DrinkIngredientInline(admin.TabularInline):
    model = DrinkIngredient

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    inlines = (DrinkIngredientInline,)

admin.site.register(Drink, DrinkAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author')

admin.site.register(Comment, CommentAdmin)

