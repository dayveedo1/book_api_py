from django.contrib import admin
from django.urls import path
from book_api.views import books_list
from book_api.views import book_add
from book_api.views import book

urlpatterns = [
    path('list/', books_list),   # books_list url (GET)
    path('', book_add),          #book_add url (POST)
    path('<int:pk>', book)       #book url (GET BY ID)

]
