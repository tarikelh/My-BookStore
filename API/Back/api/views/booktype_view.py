from django.http import JsonResponse
from ..models.BookType import BookType
from ..dao.booktype_dao import BookTypeDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class BookTypesView(View):
    """View class for retrieving all BookTypes."""

    def get(self, request):
        """Handle GET requests to retrieve all BookTypes."""
        bookTypes = BookTypeDAO.get_all(BookType)
        return JsonResponse({'success': True, 'data': list(bookTypes.values())})
   
class BookTypeView(View):
    """View class for retrieving, creating, updating, and deleting BookTypes."""

    def get(self, request, bookType_id):
        """Handle GET requests to retrieve a specific BookType."""
        try:
            bookType = BookTypeDAO.get_by_id(BookType, bookType_id)
            return JsonResponse({'success': True, 'data': bookType.to_json()})
        except BookType.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le Type de livre spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create a BookType."""
        try:
            data = json.loads(request.body)
            bookType = BookTypeDAO.save_or_update(BookType, data) #, _ => Extraction de l'objet BookType du tuple
            return JsonResponse({'success': True, 'data': bookType.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, bookType_id):
        """Handle PUT requests to update a BookType."""
        try:
            data = json.loads(request.body)
            data['id'] = bookType_id
            bookType, _ = BookTypeDAO.save_or_update(BookType, data) #, _ => Extraction de l'objet BookType du tuple
            return JsonResponse({'success': True, 'data': bookType.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, bookType_id):
        """Handle DELETE requests to delete a BookType."""
        try:
            BookTypeDAO.delete_by_id(BookType, bookType_id)
            return JsonResponse({'success': True, 'message': 'Type de livre supprimé avec succès'})
        except BookType.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le Type de livre spécifié n\'existe pas'}, status=404)