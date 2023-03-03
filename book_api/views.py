"""
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
    try:
        book_get = Book.objects.get(pk=pk)
    except:
        return Response({
            "error": "Book Not Found"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':                                        # get book by ID (pk = ID)
        #book_get = Book.objects.get(pk=pk)                             # serialize and return response
        serializer = BookSerializer(book_get)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':                                        # update by ID (PUT request)
        #book_get = Book.objects.get(pk=pk)
        serializer = BookSerializer(book_get, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        #book_get = Book.objects.get(pk=pk)
        book_get.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


#### NEW STRUCTURE #######
from rest_framework.views import APIView            #import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):                                    # create a class to inherit from APIView
    def get(self, request):                                 # get request
        books = Book.objects.all()                          # complex data
        serializer = BookSerializer(books, many=True)       # serialize from complex data to JSON
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookCreate(APIView):                                                      # create a class to inherit from APIView
    def post(self, request):                                                    # post request
        serializer = BookSerializer(data=request.data)                          # serialize data from JSON to complex data
        if serializer.is_valid():                                               # check if data supplied is valid
            serializer.save()                                                   # save to DB
            return Response(serializer.data, status=status.HTTP_200_OK)         # return a response of saved data
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)  # return validation errors if invalid


class BookDetails(APIView):                                     # class for GET BY ID, PUT & DELETE

    # function to get book by ID
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                "error": "Book Not Found"
            }, status=status.HTTP_404_NOT_FOUND)


    # GET BY ID Endpoint
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # PUT Endpoint
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE Endpoint
    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response({
            "DELETED": True
        }, status=status.HTTP_204_NO_CONTENT)


    
 

