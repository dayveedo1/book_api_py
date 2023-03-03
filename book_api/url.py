from django.contrib import admin
from django.urls import path
#from book_api.views import books_list
#from book_api.views import book_add
#from book_api.views import book
from book_api.views import BookList, BookCreate, BookDetails

urlpatterns = [
    #path('list/', books_list),   # books_list url (GET)
    #path('', book_add),          #book_add url (POST)
    #path('<int:pk>', book)       #book url (GET BY ID)

    ### NEW STRUCTURE ###
    path('list/', BookList.as_view()),        # books_list url (GET)
    path('', BookCreate.as_view()),               #book_add url (POST)
    path('<int:pk>', BookDetails.as_view())       #book url (GET BY ID)
]
