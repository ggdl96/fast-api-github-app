from core.constants.base_config import settings
import time
import jwt


def generate_jwt() -> str:
    """Generation of JWT

    Returns:
        str: Encoded JWT
    """
    with open(settings.GITHUB_PRIVATE_KEY, 'rb') as pem_file:
        signing_key = pem_file.read()

        payload = {
            # Issued at time
            'iat': int(time.time()),
            # JWT expiration time (10 minutes maximum)
            'exp': int(time.time()) + 500,
            # GitHub App's client ID
            'iss': settings.APP_ID,
        }

        encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')
        
        return encoded_jwt

def create_access_token(data: dict[str]) -> str:
    """Creates an JWT Access token for authorizing product endpoint

    Args:
        data (str, optional): Data for generating the JWT Token. Defaults to dict[str].

    Returns:
        str: Encoded JWT
    """
    with open(settings.GITHUB_PRIVATE_KEY, 'rb') as pem_file:
        signing_key = pem_file.read()
        payload = {
            **data,
            "aud": settings.AUD_JWT,
            # Issued at time
            'iat': int(time.time()),
            # JWT expiration time (10 minutes maximum)
            'exp': 300,
            # GitHub App's client ID
            'iss': settings.GTHUB_ISS_JWT,
        }

        encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')
        
        return encoded_jwt
