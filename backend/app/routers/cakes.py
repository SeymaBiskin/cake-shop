from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from app.models import Cake, CakeCreate
from app.util.logger_factory import LoggerFactory

from app.database import (
    fetch_one_cake,
    fetch_all_cakes,
    create_cake,
    update_cake,
    delete_cake
)

router = APIRouter()
log = LoggerFactory().logger


@router.get("/cake", summary="Get cakes", status_code=200)
async def get_cake():
    log.info("Received GET cake request")
    response = await fetch_all_cakes()
    log.info("Successfully fetched all cakes")
    return response


@router.get("/cake{id}/", response_model=Cake, summary="Get cake", status_code=200)
async def get_cake_by_id(id: str):
    log.info(f"Received GET cake request with id: {id}")
    response = await fetch_one_cake(id)
    if response:
        log.info(f"Successfully retrieved cake with id: {id}")
        return response
    log.warning(f"There is no cake with id {id}")
    raise HTTPException(404, f"There is no cake with id {id}")


@router.post("/cake", response_model=CakeCreate, summary="Add cake", status_code=201)
async def post_cake(cake: CakeCreate = Body(...)):
    log.info(f"Received POST request to add a new cake: {cake}")
    cake_dict = jsonable_encoder(cake)
    cake_dict["_id"] = (ObjectId())
    response = await create_cake(cake_dict)
    if response:
        log.info(f"Successfully inserted a new cake")
        return response
    log.warning("Wrong data entered/ Bad request")
    raise HTTPException(400, "Wrong data entered/ Bad request")


@router.put("/cake{id}/", response_model=Cake, summary="Update cake", status_code=200)
async def update_cake_by_id(id: str, name: str, comment: str, image_url: str, yum_factor: int):
    log.info(f"Received PUT request to update cake with id: {id}")
    response = await update_cake(id, name, comment, image_url, yum_factor)
    if response:
        log.info(f"Successfully updated cake with id: {id}")
        return response
    log.warning(f"There is no cake with id: {id} to update")
    raise HTTPException(404, f"There is no cake with id: {id} to update")


@router.delete("/cake{id}", summary="Delete cake", status_code=204)
async def delete_cake_by_id(id: str):
    log.info(f"Received DELETE request to remove cake with id: {id}")
    response = await delete_cake(id)
    if response:
        message = f"Succesfully deleted cake with id {id}"
        log.info(message)
        return message
    log.warning(f"There is no cake with id: {id}")
    raise HTTPException(404, f"There is no cake with id {id}")
