from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

def validate_user(data: list[dict]) -> list[User]:
    validated_users = []

    for item in data:
        user = User(**item) #Tạo một instance của User bằng cách unpacking dictionary user
        validated_users.append(user) #Thêm user đã được xác thực vào danh sách validated_users
        
    return validated_users