from django.contrib import admin


# Register your models here.
from .models.Product import Product
from .models.User import User
from .models.Author import Author
from .models.Book import Book
from .models.BookType import BookType
from .models.Editor import Editor
from .models.Order import Order
from .models.Order_Product import Order_Product

#admin.site.register()
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Product)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookType)
admin.site.register(Editor)
