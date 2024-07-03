import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings

class JWT:

    def generate_jwt_token(payload):
        """
        Generate a JWT token with the given payload.

        Args:
            payload (dict): The payload to be encoded in the JWT token.

        Returns:
            str: The generated JWT token.
        """
        payload['exp'] = datetime.now(timezone.utc) + timedelta(days=1)
        return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    def decode_jwt_token(token):
        """
        Decode a JWT token.

        Args:
            token (str): The JWT token to decode.

        Returns:
            dict: The decoded payload of the JWT token.
        """
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])