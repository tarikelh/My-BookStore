from django.http import JsonResponse
from ..models.Author import Author
from ..dao.author_dao import AuthorDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class AuthorsView(View):
    """View class for retrieving all Authors."""

    def get(self, request):
        """Handle GET requests to retrieve all Authors."""
        authors = AuthorDAO.get_all(Author)
        return JsonResponse({'success': True, 'data': list(authors.values())})
   
class AuthorView(View):
    """View class for retrieving, creating, updating, and deleting Authors."""

    def get(self, request, author_id):
        """Handle GET requests to retrieve a specific Author."""
        try:
            author = AuthorDAO.get_by_id(Author, author_id)
            return JsonResponse({'success': True, 'data': author.to_json()})
        except Author.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'auteur spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create an Author."""
        try:
            data = json.loads(request.body)
            author = AuthorDAO.save_or_update(Author, data) #, _ => Extraction de l'objet Author du tuple
            return JsonResponse({'success': True, 'data': author.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, author_id):
        """Handle PUT requests to update an Author."""
        try:
            data = json.loads(request.body)
            data['id'] = author_id
            author, _ = AuthorDAO.save_or_update(Author, data) #, _ => Extraction de l'objet Author du tuple
            return JsonResponse({'success': True, 'data': author.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, author_id):
        """Handle DELETE requests to delete an Author."""
        try:
            AuthorDAO.delete_by_id(Author, author_id)
            return JsonResponse({'success': True, 'message': 'Auteur supprimé avec succès'})
        except Author.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'auteur spécifié n\'existe pas'}, status=404)