class CrudDAO:
    """Data Access Object (DAO) for CRUD operations."""

    @staticmethod
    def get_by_id(cls, id):
        """Retrieve an object by its ID."""
        return cls.objects.get(pk=id)

    @staticmethod
    def get_all(cls):
        """Retrieve all objects of a class."""
        return cls.objects.all()

    @staticmethod
    def save_or_update(cls, data):
        """
        Save or update an object.

        If the data contains an 'id', update the existing object.
        Otherwise, create a new object.
        """
        if 'id' in data:
            instance = cls.objects.update_or_create(pk=data['id'], defaults=data)
        else:
            instance = cls.objects.create(**data)
        return instance

    @staticmethod
    def delete_by_id(cls, id):
        """Delete an object by its ID."""
        instance = cls.objects.get(pk=id)
        instance.delete()
