from store.users import USERS
from models.users import User

def user_by_owner(owner: str) -> User | None:
    """Get User by Owner

    Args:
        owner (str): username

    Returns:
        User | None: user object or None
    """
    return next((u for u in USERS if u["user_name"] == owner), None)
