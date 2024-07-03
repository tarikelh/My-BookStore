"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views.product_view import ProductsView, ProductView
from .views.user_view import UsersView, UserView
from .views.csrf_view import GetCSRFToken
from .views.auth_view import LoginView, RegisterView
from .views.order_view import OrdersView, OrderView
from .views.order_product_view import OrdersProductsView, OrderProductView
from .views.book_view import BooksView, BookView
from .views.author_view import AuthorsView, AuthorView
from .views.editor_view import EditorsView, EditorView
from .views.booktype_view import BookTypesView, BookTypeView
#from .views.crud_user_view import CrudUserView

"""URL patterns for the API endpoints.

These URL patterns define the routes for accessing the API resources. 
To access these endpoints, prefix them with 'api/', for example, 'api/products'.
"""

urlpatterns = [
    #products
    path('products', ProductsView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductView.as_view(), name = 'product-detail'),
    path('products/', ProductView.as_view(), name='product-create'),
    path('products/<int:product_id>', ProductView.as_view(), name='product-update'),
    path('products/<int:product_id>', ProductView.as_view(), name='product-delete'),
    #users
    path('users', UsersView.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserView.as_view(), name='user-detail'),
    path('users/<int:user_id>', UserView.as_view(), name='user-update'),
    path('users/<int:user_id>', UserView.as_view(), name='user-delete'),
    
    #csrf
    path('csrf/', GetCSRFToken.as_view()),

    #login - register
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),

    #orders
    path('orders', OrdersView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderView.as_view(), name = 'order-detail'),
    path('orders/', OrderView.as_view(), name='order-create'),
    path('orders/<int:order_id>', OrderView.as_view(), name='order-update'),
    path('orders/<int:order_id>', OrderView.as_view(), name='order-delete'),
    #orders_products
    path('orders_products', OrdersProductsView.as_view(), name='command-list'),
    path('orders_products/<int:o_product_id>/', OrderProductView.as_view(), name = 'command-detail'),
    path('orders_products/', OrderProductView.as_view(), name='command-create'),
    path('orders_products/<int:o_product_id>', OrderProductView.as_view(), name='command-update'),
    path('orders_products/<int:o_product_id>', OrderProductView.as_view(), name='command-delete'),
    #books
    path('books', BooksView.as_view(), name='book-list'),
    path('books/<int:book_id>/', BookView.as_view(), name = 'book-detail'),
    path('books/', BookView.as_view(), name='book-create'),
    path('books/<int:book_id>', BookView.as_view(), name='book-update'),
    path('books/<int:book_id>', BookView.as_view(), name='book-delete'),
    #authors
    path('authors', AuthorsView.as_view(), name='author-list'),
    path('authors/<int:author_id>/', AuthorView.as_view(), name = 'author-detail'),
    path('authors/', AuthorView.as_view(), name='author-create'),
    path('authors/<int:author_id>', AuthorView.as_view(), name='author-update'),
    path('authors/<int:author_id>', AuthorView.as_view(), name='author-delete'),
    #editors
    path('editors', EditorsView.as_view(), name='editor-list'),
    path('editors/<int:editor_id>/', EditorView.as_view(), name = 'editor-detail'),
    path('editors/', EditorView.as_view(), name='editor-create'),
    path('editors/<int:editor_id>', EditorView.as_view(), name='editor-update'),
    path('editors/<int:editor_id>', EditorView.as_view(), name='editor-delete'),
    #booktypes
    path('booktypes', BookTypesView.as_view(), name='booktype-list'),
    path('booktypes/<int:booktype_id>/', BookTypeView.as_view(), name = 'booktype-detail'),
    path('booktypes/', BookTypeView.as_view(), name='booktype-create'),
    path('booktypes/<int:booktype_id>', BookTypeView.as_view(), name='booktype-update'),
    path('booktypes/<int:booktype_id>', BookTypeView.as_view(), name='booktype-delete'),


    #manage user
    #path('crudusers/', CrudUserView.as_view())

]
