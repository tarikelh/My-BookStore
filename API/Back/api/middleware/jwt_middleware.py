from ..utils.jwt_util import JWT
import jwt
from functools import wraps
from ..utils.error_handler_util import InvalidTokenOrRequiredError

def jwt_middleware(view_func):
    """
    Middleware to decode JWT token from request header and attach payload to request.

    Args:
        view_func (function): The view function to be wrapped.

    Raises:
        InvalidTokenOrRequiredError: If the token is missing or invalid.

    Returns:
        function: Decorated function.
    """
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token or not token.startswith('Bearer '):
            raise InvalidTokenOrRequiredError()

        token = token.split(' ')[1]
        try:
            # Décoder le token pour obtenir les informations
            payload = JWT.decode_jwt_token(token)
            request.jwt_payload = payload  # Stocker le payload dans la requête pour y accéder dans le décorateur
            return view_func(self, request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            raise InvalidTokenOrRequiredError('Le token a expiré')
        except jwt.InvalidTokenError:
            raise InvalidTokenOrRequiredError('Token invalide')
        except KeyError:
            raise InvalidTokenOrRequiredError('Clé manquante dans le payload du token')
    return wrapper
