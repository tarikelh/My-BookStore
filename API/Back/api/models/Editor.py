from django.db import models

class Editor(models.Model):
    name = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }