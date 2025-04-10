from core.constants.base_config import settings
import time
import jwt

from models.github import GithubActionJWTDecoded


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
            'exp': int(time.time()) + 5000,
            # GitHub App's client ID
            'iss': settings.GTHUB_ISS_JWT,
        }

        encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')

        return encoded_jwt

def github_jwt_validation(decoded_token: GithubActionJWTDecoded) -> bool:
    """Validate JWT from github actions

    Args:
        decoded_token (_type_): The decoded JWT token
        provider_user_id (str): The id of the User in the provider

    Returns:
        bool: The validation result
    """
    return decoded_token.aud == settings.AUD_JWT and decoded_token.iss == settings.GTHUB_ISS_JWT and time.time() < decoded_token.exp
