from django.http import JsonResponse
from ..models.Order import Order
from ..dao.order_dao import OrderDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class OrdersView(View):
    """View class for retrieving all Orders."""

    def get(self, request):
        """Handle GET requests to retrieve all Orders."""
        orders = OrderDAO.get_all(Order)
        return JsonResponse({'success': True, 'data': list(orders.values())})
   
class OrderView(View):
    """View class for retrieving, creating, updating, and deleting Orders."""

    def get(self, request, order_id):
        """Handle GET requests to retrieve a specific Order."""
        try:
            order = OrderDAO.get_by_id(Order, order_id)
            return JsonResponse({'success': True, 'data': order.to_json()})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'la commande spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create an Order."""
        try:
            data = json.loads(request.body)
            order = OrderDAO.save_or_update(Order, data) #, _ => Extraction de l'objet Order du tuple
            return JsonResponse({'success': True, 'data': order.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, order_id):
        """Handle PUT requests to update an Order."""
        try:
            data = json.loads(request.body)
            data['id'] = order_id
            order, _ = OrderDAO.save_or_update(Order, data) #, _ => Extraction de l'objet Order du tuple
            return JsonResponse({'success': True, 'data': order.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, order_id):
        """Handle DELETE requests to delete an Order."""
        try:
            OrderDAO.delete_by_id(Order, order_id)
            return JsonResponse({'success': True, 'message': 'Commande supprimée avec succès'})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'la commande spécifié n\'existe pas'}, status=404)