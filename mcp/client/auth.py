# Simple mock identity store (later this can be JWT / OAuth / DB)

USERS = {
    "anil": {"role": "admin"},
    "guest": {"role": "user"},
    "dev": {"role": "developer"}
}

def get_user(username: str):
    return USERS.get(username, {"role": "guest"})
