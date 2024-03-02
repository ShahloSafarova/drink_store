from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Drink, DrinkIngredient, Ingredient, Comment, Category
from .serializers import DrinkSerializer, CommentSerializer, DrinkIngredientSerializer, IngredientSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied


class DrinkListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        drinks = Drink.objects.all()
        paginator = Paginator(drinks, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = DrinkSerializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "Only admins can use it."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Hooraaay, added!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed!!!"}, status=status.HTTP_400_BAD_REQUEST)


#
class DrinkRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Drink.objects.get(pk=pk)
        except Drink.DoesNotExist:
            raise NotFound("Not Found!")

    def get(self, request, pk):
        drink = self.get_object(pk=pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        drink = self.get_object(pk=pk)
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Information was successfully changed", serializer.data)
        return Response("Unsuccessful attempt", serializer.errors)

    def patch(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        drink = self.get_object(pk=pk)
        serializer = DrinkSerializer(drink, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Done", serializer.data)
        return Response("Undone", serializer.errors)

    def delete(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        drink = self.get_object(pk=pk)
        drink.delete()
        return Response("Successfully deleted!", status=status.HTTP_204_NO_CONTENT)

class DrinkIngredientsListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ingredient = DrinkIngredient.objects.all()
        paginator = Paginator(ingredient, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = DrinkIngredientSerializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "Only admins can use it."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = DrinkIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Hooraaay, added!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed!!!"}, status=status.HTTP_400_BAD_REQUEST)


#
class DrinkIngredientsRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return DrinkIngredient.objects.get(pk=pk)
        except DrinkIngredient.DoesNotExist:
            raise NotFound("Not Found!")

    def get(self, request, pk):
        ingredients = self.get_object(pk=pk)
        serializer = DrinkIngredientSerializer(ingredients)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredients = self.get_object(pk=pk)
        serializer = DrinkIngredientSerializer(ingredients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Information was successfully changed", serializer.data)
        return Response("Unsuccessful attempt", serializer.errors)

    def patch(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredients = self.get_object(pk=pk)
        serializer = DrinkIngredientSerializer(ingredients, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Done", serializer.data)
        return Response("Undone", serializer.errors)

    def delete(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredients = self.get_object(pk=pk)
        ingredients.delete()
        return Response("Successfully deleted!", status=status.HTTP_204_NO_CONTENT)

class IngredientsListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ingredient = Ingredient.objects.all()
        paginator = Paginator(ingredient, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = IngredientSerializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "Only admins can use it."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Hooraaay, added!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed!!!"}, status=status.HTTP_400_BAD_REQUEST)


#
class IngredientsRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise NotFound("Not Found!")

    def get(self, request, pk):
        ingredient = self.get_object(pk=pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredient = self.get_object(pk=pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Information was successfully changed", serializer.data)
        return Response("Unsuccessful attempt", serializer.errors)

    def patch(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredient = self.get_object(pk=pk)
        serializer = IngredientSerializer(ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Done", serializer.data)
        return Response("Undone", serializer.errors)

    def delete(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to change it!")
        ingredient = self.get_object(pk=pk)
        ingredient.delete()
        return Response("Successfully deleted!", status=status.HTTP_204_NO_CONTENT)

class CategoryListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        paginator = Paginator(categories, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = CategorySerializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "Only admins can use it."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound("Category not found!")

    def get(self, request, pk):
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to modify categories.")
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Category information updated successfully.", serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to modify categories.")
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Category information updated successfully.", serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.is_staff:
            raise PermissionDenied("Only admins are able to delete categories.")
        category = self.get_object(pk=pk)
        category.delete()
        return Response("Category deleted successfully.", status=status.HTTP_204_NO_CONTENT)


class UserCommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        comments = Comment.objects.filter(author=user)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404("Sharh topilmadi!")

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Changed", serializer.data)
        return Response("Failed!", serializer.errors)

    def patch(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Changed", serializer.data)
        return Response("Undone due some mistakes!", serializer.errors)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response("Successfully deleted!", status=status.HTTP_204_NO_CONTENT)


