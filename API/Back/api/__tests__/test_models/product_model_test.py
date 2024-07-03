from django.test import TestCase
from ...models.Product import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            photo='test.jpg',
            price=9.99
        )
    
    def test_to_json(self):
        """Test the to_json method of Product model"""
        expected_json = {
            'id': self.product.id,
            'name': 'Test Product',
            'description': 'Test Description',
            'photo': 'test.jpg',
            'price': '9.99',
        }
        self.assertEqual(self.product.to_json(), expected_json)