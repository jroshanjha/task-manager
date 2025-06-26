from pydantic import BaseModel,EmailStr,NameEmail,Field,validator,constr,root_validator
import re

# Pydantic Model
class UserCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=2, max_length=50)
    email: EmailStr
    
    @validator('name')
    def validate_name(cls, v):
        if not re.match("^[A-Za-z ]+$", v):
            raise ValueError('Name must contain only letters and spaces')
        return v

# class UserOut(UserCreate):
#     id: int

#     class Config:
#         orm_mode = True
class UserOut(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

#     class Config:
#         orm_mode = True

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
        