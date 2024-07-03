from django.db import models

class Order_Product(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'product')

    def to_json(self):
        return {
            'order_id': self.order.id,
            'product_id': self.product.id,
            'quantity': self.quantity,
            'product': self.product.to_json()
        }
