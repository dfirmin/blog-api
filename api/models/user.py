from ..models.pyobjectid import PyObjectId
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  name: str = Field(...)
  email: EmailStr = Field(...)
  password: str = Field(...)

  class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      json_encoders = {ObjectId: str}
      schema_extra = {
          "example": {
              "name": "Jane Doe",
              "email": "jdoe@example.com",
              "password": "secret_code"
          }
      }

class UserResponseModel(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  name: str = Field(...)
  email: EmailStr = Field(...)

  class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      json_encoders = {ObjectId: str}
      schema_extra = {
          "example": {
              "name": "Jane Doe",
              "email": "jdoe@example.com"
          }
      }
