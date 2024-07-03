from django.http import JsonResponse
from ..models.User import User
from ..dao.user_dao import UserDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class UsersView(View):
    """View class for retrieving all users."""

    @check_permission(['admin'])
    def get(self, request):
        """Handle GET requests to retrieve all users."""
        users = UserDAO.get_all(User)
        return JsonResponse({'success': True, 'data': list(users.values())})

class UserView(View):
    """View class for retrieving, updating, and deleting users."""

    @check_permission(['admin', 'user'])
    def get(self, request, user_id):
        """Handle GET requests to retrieve a specific user."""
        try:
            user = UserDAO.get_by_id(User, user_id)
            return JsonResponse({'success': True, 'data': user.to_json()})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'utilisateur spécifié n\'existe pas'}, status=404)

    @check_permission(['admin', 'user'])
    def put(self, request, user_id):
        """Handle PUT requests to update a user."""
        try:
            data = json.loads(request.body)
            data['id'] = user_id 
            user, _ = UserDAO.save_or_update(User, data) #, _ => Extraction de l'objet User du tuple
            return JsonResponse({'success': True, 'data': user.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    @check_permission(['admin', 'user'])
    def delete(self, request, user_id):
        """Handle DELETE requests to delete a user."""
        try:
            UserDAO.delete_by_id(User, user_id)
            return JsonResponse({'success': True, 'message': 'Utilisateur supprimé avec succès'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'utilisateur spécifié n\'existe pas'}, status=404)