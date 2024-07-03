from django.db import models

class Author(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'lastname': self.lastname,
            'firstname': self.firstname,
        }