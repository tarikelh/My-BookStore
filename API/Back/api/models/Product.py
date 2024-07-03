from django.db import models

class Product(models.Model):
    """ Product Entity """
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    photo = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'photo': self.photo,
            'price': str(self.price), 
        }