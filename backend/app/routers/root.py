from fastapi import APIRouter

router = APIRouter()


@router.get('/', summary= "Welcome page")
async def root():
    return {'message': 'Hello from Cake Shop'}