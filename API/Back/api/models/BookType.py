from django.db import models

class BookType(models.Model):
    label = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'label': self.label,
        }