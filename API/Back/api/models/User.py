from django.db import models
from django.contrib.auth.hashers import check_password as check_password_django


class User(models.Model):
    """ User Entity """
    ROLES = (
        ('user', 'Utilisateur'),
        ('admin', 'Administrateur'),
    )

    lastname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50, choices = ROLES)

    def check_password(self, raw_password):
        return check_password_django(raw_password, self.password)

    def to_json(self):
        return {
            'id': self.id,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'email': self.email,
            'password': self.password,
            'role': self.role,
        }