from store.users import USERS, USERS_PRODUCT
from models.users import User, ProductUserLogin

def user_by_owner(owner: str) -> User | None:
    """Get User by Owner

    Args:
        owner (str): username

    Returns:
        User | None: user object or None
    """
    return next((u for u in USERS if u["user_name"] == owner), None)

def product_user_by_name(name: str) -> ProductUserLogin | None:
    """Get Product User by Name

    Args:
        name (str): username

    Returns:
        User | None: user object or None
    """
    user = next((u for u in USERS_PRODUCT if u["username"] == name), None)
    
    if (user):
        return ProductUserLogin(username=user["username"], password=user["password"], provider_user_id=user["provider_user_id"], provider=user["provider"])
