from typing import List, Optional

from fastapi import APIRouter, HTTPException
from app.models import Cake

from app.database import (
    fetch_one_cake,
    fetch_all_cakes,
    create_cake,
    update_cake,
    remove_cake
)

router = APIRouter()


@router.get("/cake", summary= "Get cakes")
async def get_cake():
    response = await fetch_all_cakes()
    return response

@router.get("/cake{id}/", response_model=Cake, summary= "Get cake")
async def get_cake_by_id(id: str):
    response = await fetch_one_cake(id)
    if response:
        return response
    raise HTTPException(404, f"There is no cake with name {id}")

@router.post("/cake", response_model=Cake, summary= "Add cake")
async def post_cake(cake: Cake):
    response  = await create_cake(cake.dict())
    if response:
        return response
    raise HTTPException(400, "Wrong data entered/ Bad request")

@router.put("/cake{id}/", response_model=Cake, summary= "Update cake")
async def update_cake_by_id(id:str, name: str, comment: str, image_url: str, yum_factor: int):
    response = await update_cake(id, name, comment, image_url, yum_factor)
    if response:
        return response
    raise HTTPException(404, f"There is no cake with name {name}")

@router.delete("/cake{id}", summary= "Delete cake")
async def delete_cake_by_id(id: str):
    response = await remove_cake(id)
    if response:
        return f"Succesfully deleted cake with id {id}"
    raise HTTPException(404, f"There is no cake with id {id}")
