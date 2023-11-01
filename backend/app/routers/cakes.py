from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from app.models import Cake, CakeCreate
from typing import Optional

from app.database import (
    fetch_one_cake,
    fetch_all_cakes,
    create_cake,
    update_cake,
    remove_cake
)

router = APIRouter()


@router.get("/cake", summary="Get cakes", status_code=200)
async def get_cake():
    response = await fetch_all_cakes()
    return response


@router.get("/cake{id}/", response_model=Cake, summary="Get cake", status_code=200)
async def get_cake_by_id(id: str):
    response = await fetch_one_cake(id)
    if response:
        return response
    raise HTTPException(404, f"There is no cake with id {id}")


@router.post("/cake", response_model=CakeCreate, summary="Add cake", status_code=201)
async def post_cake(cake: CakeCreate = Body(...)):
    cake_dict = jsonable_encoder(cake)
    cake_dict["_id"] = (ObjectId())
    response = await create_cake(cake_dict)
    if response:
        return response
    raise HTTPException(400, "Wrong data entered/ Bad request")


@router.put("/cake{id}/", response_model=Cake, summary="Update cake", status_code=200)
async def update_cake_by_id(id: str, name: str, comment: str, image_url: str, yum_factor: int):
    response = await update_cake(id, name, comment, image_url, yum_factor)
    if response:
        return response
    raise HTTPException(404, f"There is no cake with id: {id} to update")


@router.delete("/cake{id}", summary="Delete cake", status_code=204)
async def delete_cake_by_id(id: str):
    response = await remove_cake(id)
    if response:
        return f"Succesfully deleted cake with id {id}"
    raise HTTPException(404, f"There is no cake with id {id}")
