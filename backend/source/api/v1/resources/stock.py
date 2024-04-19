from fastapi import APIRouter, status
from loguru import logger
from source.schema.stock import StockData
from typing import List
from asset.mock_data import kospi_data, kosdaq_data

router = APIRouter()


@router.get("/dummy/kospi", status_code=status.HTTP_200_OK, response_model=List[StockData], tags=["Stock"])
async def getDummyKospiData() -> List[StockData]:
    try:
        return [StockData(**data) for data in kospi_data]
    except Exception as e:
        logger.error(f"ERROR: {e}")


@router.get("/dummy/kosdaq", status_code=status.HTTP_200_OK, response_model=List[StockData], tags=["Stock"])
async def getDummyKosdaqData() -> List[StockData]:
    try:
        return [StockData(**data) for data in kosdaq_data]
    except Exception as e:
        logger.error(f"ERROR: {e}")
