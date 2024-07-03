from django.http import JsonResponse
from ..models.Editor import Editor
from ..dao.editor_dao import EditorDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class EditorsView(View):
    """View class for retrieving all Editors."""

    def get(self, request):
        """Handle GET requests to retrieve all Editors."""
        editors = EditorDAO.get_all(Editor)
        return JsonResponse({'success': True, 'data': list(editors.values())})
   
class EditorView(View):
    """View class for retrieving, creating, updating, and deleting Editors."""

    def get(self, request, editor_id):
        """Handle GET requests to retrieve an specific Editor."""
        try:
            editor = EditorDAO.get_by_id(Editor, editor_id)
            return JsonResponse({'success': True, 'data': editor.to_json()})
        except Editor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'éditeur spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create an Editor."""
        try:
            data = json.loads(request.body)
            editor = EditorDAO.save_or_update(Editor, data) #, _ => Extraction de l'objet Editor du tuple
            return JsonResponse({'success': True, 'data': editor.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, editor_id):
        """Handle PUT requests to update an Editor."""
        try:
            data = json.loads(request.body)
            data['id'] = editor_id
            editor, _ = EditorDAO.save_or_update(Editor, data) #, _ => Extraction de l'objet Editor du tuple
            return JsonResponse({'success': True, 'data': editor.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, editor_id):
        """Handle DELETE requests to delete an Editor."""
        try:
            EditorDAO.delete_by_id(Editor, editor_id)
            return JsonResponse({'success': True, 'message': 'Editeur supprimé avec succès'})
        except Editor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'L\'éditeur spécifié n\'existe pas'}, status=404)