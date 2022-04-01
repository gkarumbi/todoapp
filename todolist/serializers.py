from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Category,TodoList

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields =(
            "title",
            "content",
            "created",
            "due_date",
            "category",
        )