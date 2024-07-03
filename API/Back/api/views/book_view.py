from django.http import JsonResponse
from ..models.Book import Book
from ..dao.book_dao import BookDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class BooksView(View):
    """View class for retrieving all Books."""

    def get(self, request):
        """Handle GET requests to retrieve all Books."""
        books = BookDAO.get_all(Book)
        return JsonResponse({'success': True, 'data': list(books.values())})
   
class BookView(View):
    """View class for retrieving, creating, updating, and deleting Books."""

    def get(self, request, book_id):
        """Handle GET requests to retrieve a specific Book."""
        try:
            book = BookDAO.get_by_id(Book, book_id)
            return JsonResponse({'success': True, 'data': book.to_json()})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le livre spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create a Book."""
        try:
            data = json.loads(request.body)
            book = BookDAO.save_or_update(Book, data) #, _ => Extraction de l'objet Book du tuple
            return JsonResponse({'success': True, 'data': book.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, book_id):
        """Handle PUT requests to update a Book."""
        try:
            data = json.loads(request.body)
            data['id'] = book_id
            book, _ = BookDAO.save_or_update(Book, data) #, _ => Extraction de l'objet Book du tuple
            return JsonResponse({'success': True, 'data': book.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, book_id):
        """Handle DELETE requests to delete a Book."""
        try:
            BookDAO.delete_by_id(Book, book_id)
            return JsonResponse({'success': True, 'message': 'Livre supprimé avec succès'})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le livre spécifié n\'existe pas'}, status=404)