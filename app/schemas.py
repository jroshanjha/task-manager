from pydantic import BaseModel,EmailStr,NameEmail,Field,validator,constr,root_validator
import re

# # Pydantic Model
class UserCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=2, max_length=50)
    email: EmailStr
    
    @validator('name')
    def validate_name(cls, v):
        if not re.match("^[A-Za-z ]+$", v):
            raise ValueError('Name must contain only letters and spaces')
        return v

# # class UserCreate(BaseModel):
# #     name: str
# #     email: str

# # class UserOut(UserCreate):
# #     id: int
# #     class Config:
# #         orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True  # Pydantic v2 replacement for orm_mode=True
    }


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search("[A-Z]", v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search("[a-z]", v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search("[0-9]", v):
            raise ValueError('Password must contain at least one digit')
        if not re.search("[!@#$%^&*]", v):
            raise ValueError('Password must contain at least one special character')
        return v
    @validator('email')
    def validate_email(cls, v):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError('Invalid email format')
        return v
    
#     # class Config:
#     #     orm_mode = True

class UserLoginOut(BaseModel):
    id: int
    email: str
    
    model_config = {"from_attributes": True}  # ✅ allows serialization from SQLAlchemy objects                                        

# class UserLogin(BaseModel):
#     email: str
#     password: str

# class UserLoginOut(BaseModel):
#     id: int
#     email: str

#     model_config = {"from_attributes": True}

    
# class Token(BaseModel):
#     access_token: str
#     token_type: str

#     class Config:
#         orm_mode = True

# class Task(BaseModel):
#     title: str
#     description: str

#     class Config:
#         orm_mode = True

# class TaskCreate(Task):
#     title: str
#     description: str

#     class Config:
#         orm_mode = True

# class TaskOut(BaseModel):
#     id: int
#     title: str
#     description: str

#     class Config:
#         orm_mode = True

# class TaskUpdate(BaseModel):
#     title: str
#     description: str 

#     class Config:
#         orm_mode = True

# class TaskUpdateOut(BaseModel):
#     id: int
#     title: str
#     description: str

#     class Config:
#         orm_mode = True
        