from django.test import TestCase
from ...models.User import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            lastname='lastname User',
            firstname='firstname User',
            email='email@example.com',
            password='pass',
            role='user'
        )
    
    def test_to_json(self):
        """Test the to_json method of User model"""
        expected_json = {
            'id': self.user.id,
            'lastname': 'lastname User',
            'firstname': 'firstname User',
            'email': 'email@example.com',
            'password': 'pass',
            'role': 'Utilisateur',
        }
        self.assertEqual(self.user.to_json(), expected_json)