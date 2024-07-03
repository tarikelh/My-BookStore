from django.http import JsonResponse
from ..models.Order_Product import Order_Product
from ..dao.order_product_dao import OrderProductDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class OrdersProductsView(View):
    """View class for retrieving all orders products."""

    def get(self, request):
        """Handle GET requests to retrieve all orders products."""
        orders_products = OrderProductDAO.get_all(Order_Product)
        return JsonResponse({'success': True, 'data': list(orders_products.values())})
   
class OrderProductView(View):
    """View class for retrieving, creating, updating, and deleting orders products."""

    def get(self, request, o_product_id):
        """Handle GET requests to retrieve a specific order product."""
        try:
            o_product = OrderProductDAO.get_by_id(Order_Product, o_product_id)
            return JsonResponse({'success': True, 'data': o_product.to_json()})
        except Order_Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'La commande lié au produit spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create an order product."""
        try:
            data = json.loads(request.body)
            o_product = OrderProductDAO.save_or_update(Order_Product, data) #, _ => Extraction de l'objet Product du tuple
            return JsonResponse({'success': True, 'data': o_product.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, o_product_id):
        """Handle PUT requests to update an order product."""
        try:
            data = json.loads(request.body)
            data['id'] = o_product_id
            o_product, _ = OrderProductDAO.save_or_update(Order_Product, data) #, _ => Extraction de l'objet Product du tuple
            return JsonResponse({'success': True, 'data': o_product.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, o_product_id):
        """Handle DELETE requests to delete an order product."""
        try:
            OrderProductDAO.delete_by_id(Order_Product, o_product_id)
            return JsonResponse({'success': True, 'message': 'Commande lié au Produit supprimé avec succès'})
        except Order_Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'La commande lié au produit spécifié n\'existe pas'}, status=404)