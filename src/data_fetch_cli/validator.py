from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

def validate_user(data: list[dict]) -> list[User]:
    validated_users = []

    for item in data:
        user = User(**item)
        validated_users.append(user)
        
    return validated_users