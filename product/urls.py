from django.urls import path

from .views import (
   DrinkIngredientsListCreateAPIView, DrinkIngredientsRetrieveUpdateDestroyAPIView, DrinkListCreateAPIView,  DrinkRetrieveUpdateDestroyAPIView, UserCommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView, IngredientsListCreateAPIView, IngredientsRetrieveUpdateDestroyAPIView, CategoryRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView
)

urlpatterns = [
    path('drinks/', DrinkListCreateAPIView.as_view(), name='drink-list-create'),
    path('drink/<int:pk>', DrinkRetrieveUpdateDestroyAPIView.as_view(), name='drink-detail'),

    path('ingredient/<int:pk>', DrinkIngredientsListCreateAPIView.as_view(), name='drink-ingredients-list-create'),
    path('ingredients/<int:pk>', DrinkIngredientsRetrieveUpdateDestroyAPIView.as_view(), name='drink-ingredients-detail'),

    path('ingredient/<int:pk>', IngredientsListCreateAPIView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>', IngredientsRetrieveUpdateDestroyAPIView.as_view(), name='ingredient-detail'),

    path('categories/<int:pk>', CategoryListCreateAPIView.as_view(), name='categories-list-create'),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),


    path('comments/', UserCommentListCreateAPIView.as_view(), name='user-comment-list-create'),
    path('comments/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
