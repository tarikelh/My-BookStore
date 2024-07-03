from django.db import models

class Order(models.Model):
    """ Order Entity """
    STATES = (
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée')
    )

    order_date = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=STATES, default='en_attente')
    total_order = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='Order_Product')

    def to_json(self):
        return {
            'id': self.id,
            'order_date': self.order_date,
            'state': self.state,
            'total_order': self.total_order,
            'user_id': self.user.id,
            'products': [ op.to_json() for op in self.order_product_set.all()]
        }