from django.http import JsonResponse
from ..models.Product import Product
from ..dao.product_dao import ProductDAO
import json
from django.views import View
from ..utils.decorator_util import check_permission

class ProductsView(View):
    """View class for retrieving all products."""

    def get(self, request):
        """Handle GET requests to retrieve all products."""
        products = ProductDAO.get_all(Product)
        return JsonResponse({'success': True, 'data': list(products.values())})
   
class ProductView(View):
    """View class for retrieving, creating, updating, and deleting products."""

    def get(self, request, product_id):
        """Handle GET requests to retrieve a specific product."""
        try:
            product = ProductDAO.get_by_id(Product, product_id)
            return JsonResponse({'success': True, 'data': product.to_json()})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le produit spécifié n\'existe pas'}, status=404)
    
    @check_permission(['admin'])    
    def post(self, request):
        """Handle POST requests to create a product."""
        try:
            data = json.loads(request.body)
            product = ProductDAO.save_or_update(Product, data) #, _ => Extraction de l'objet Product du tuple
            return JsonResponse({'success': True, 'data': product.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def put(self, request, product_id):
        """Handle PUT requests to update a product."""
        try:
            data = json.loads(request.body)
            data['id'] = product_id
            product, _ = ProductDAO.save_or_update(Product, data) #, _ => Extraction de l'objet Product du tuple
            return JsonResponse({'success': True, 'data': product.to_json()})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    @check_permission(['admin'])
    def delete(self, request, product_id):
        """Handle DELETE requests to delete a product."""
        try:
            ProductDAO.delete_by_id(Product, product_id)
            return JsonResponse({'success': True, 'message': 'Produit supprimé avec succès'})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Le produit spécifié n\'existe pas'}, status=404)