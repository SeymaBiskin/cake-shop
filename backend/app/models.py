from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Cake(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., description="The name lenght can be maximum maximum 30", max_length=30)
    comment: str = Field(..., title="The comment lenght can be maximum 200", max_length=200)
    imageUrl: str = Field(..., title="Url for the image")
    yumFactor: int = Field(..., title="YumFactor rating from 1 to 5", ge=1, le=5)

    class Config:
        json_encoders = {ObjectId: str}


class CakeCreate(BaseModel):
    name: str = Field(..., description="The name lenght can be maximum maximum 30", max_length=30)
    comment: str = Field(..., title="The comment lenght can be maximum 200", max_length=200)
    imageUrl: str = Field(..., title="Url for the image")
    yumFactor: int = Field(..., title="YumFactor rating from 1 to 5", ge=1, le=5)
