from functools import wraps
from ..middleware.jwt_middleware import jwt_middleware
from ..utils.error_handler_util import UnauthorizedError, UserIdMismatchError

def check_permission(allowed_roles):
    """
    Decorator to check user permissions based on allowed roles.

    Args:
        allowed_roles (list): List of roles allowed to access the resource.

    Raises:
        UnauthorizedError: If the user does not have the necessary permissions.
        UserIdMismatchError: If the user ID in the token does not match the request.

    Returns:
        function: Decorated function.
    """
    def decorator(view_func):
        @wraps(view_func)
        @jwt_middleware
        def wrapper(self, request, *args, **kwargs):
            payload = request.jwt_payload

            # Vérifier le rôle de l'utilisateur
            if payload['role'] not in allowed_roles:
                raise UnauthorizedError()
            
            user_id_from_token = payload['user_id']
            if kwargs.get('user_id'):
                user_id_from_request = kwargs.get('user_id')
                if user_id_from_token != user_id_from_request and payload['role'] == 'user':
                    raise UserIdMismatchError()

            # Autoriser l'accès si les autorisations sont valides
            return view_func(self, request, *args, **kwargs)
        return wrapper
    return decorator
