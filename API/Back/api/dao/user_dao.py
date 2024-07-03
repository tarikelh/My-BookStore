from ..models.User import User
from .crud_dao import CrudDAO
from django.contrib.auth.hashers import make_password

class UserDAO(CrudDAO):
    """Data Access Object (DAO) for User model."""

    @staticmethod
    def get_user_by_email(email):
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user object if found, None otherwise.
        """
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def save_or_update(cls, data):
        """
        Save or update a user object.

        If the data contains a 'password', hash it before saving or updating.

        Args:
            cls: The User class.
            data (dict): Dictionary containing user data.

        Returns:
            User: The saved or updated user object.
        """
        if 'password' in data:
            # Utiliser make_password pour hacher le mot de passe
            # Mettre à jour les données avec le mot de passe haché
            data['password'] = make_password(data['password'])

        if 'id' in data:
            instance = cls.objects.update_or_create(pk=data['id'], defaults=data)
        else:
            instance = cls.objects.create(**data)
        return instance