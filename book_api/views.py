from django.shortcuts import render
from django.http import JsonResponse
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

# GET ALL REQUEST
@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()                                      #complex data
    serializer = BookSerializer(books, many=True)                   #serialize from complex data to JSON
    return Response(serializer.data, status=status.HTTP_200_OK)


# POST REQUEST
@api_view(['POST'])
def book_add(request):
    serializer = BookSerializer(data=request.data)                     #serialize data from JSON to complex data
    if serializer.is_valid():                                          #check if data supplied is valid
        serializer.save()                                              #save to DB
        return Response(serializer.data, status=status.HTTP_200_OK)                               #return a response of saved data
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                             #return validation errors if invalid



@api_view(['GET','PUT','DELETE'])
def book(request, pk):
    if request.method == 'GET':                                        # get book by ID (pk = ID)
        book_get = Book.objects.get(pk=pk)                             # serialize and return response
        serializer = BookSerializer(book_get)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':                                        # update by ID (PUT request)
        book_get = Book.objects.get(pk=pk)
        serializer = BookSerializer(book_get, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book_get = Book.objects.get(pk=pk)
        book_get.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


