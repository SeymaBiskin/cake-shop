from pydantic import BaseModel, Field
from typing import Dict
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Cake(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., title="Name of the cake", max_length=30)
    comment: str = Field(..., title="Description of the cake", max_length=200)
    imageUrl: str = Field(..., title="Url for the image")
    yumFactor: int = Field(..., title="YumFactor rating frm 1 to 5", ge=1, le=5)

    class Config:
        allow_population_by_field_name = False
        arbitrary_types_allowed = True 