from fastapi import APIRouter, status

from source.schema.dummy import DummyResponse

router = APIRouter()


@router.get("/dummy", response_model=DummyResponse, status_code=status.HTTP_200_OK, tags=["Dummy"])
async def getDummy() -> DummyResponse:

    response = DummyResponse(status="ok", data_str="dummy_text", data_int=1, data_float=0.1)
    return response
