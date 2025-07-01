import secrets
from string import ascii_letters, digits

def generate_short_key(length: int = 6) -> str:
    pool = ascii_letters + digits
    return ''.join(secrets.choice(pool) for i in range(length))