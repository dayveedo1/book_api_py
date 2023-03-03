"""
from rest_framework import serializers
from book_api.models import Book


#serialize data from complex data to JSON
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField()
    quantity = serializers.IntegerField()


    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.published_date = data.get('published_date', instance.published_date)
        instance.quantity = data.get('quantity', instance.quantity)

        instance.save()
        return instance
"""

### Re-defining the Serializers to inherit from ModelSerializers

from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


    def validate_title(self, value):                                           # perform custom validation on a specific field in the model
        if value == "Diet Coke":
            raise ValidationError(f"{value} cannot be registered")
        return value

    def validate(self, data):                                                   # perform custom validation on fields in model
        if data['number_of_pages'] > 200 and data['quantity'] > 200:
            raise ValidationError("To  large for inventory")
        return data
