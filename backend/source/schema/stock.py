import pydantic
from typing import Optional


class StockData(pydantic.BaseModel):

    name: str
    volume: Optional[int] = None
    price: Optional[int] = None
    open: Optional[int] = None
    close: Optional[int] = None
    high: Optional[int] = None
    low: Optional[int] = None
    foreignRate: Optional[float] = None
    marketCap: Optional[int] = None
    asset: Optional[int] = None
    debt: Optional[int] = None
    sales: Optional[int] = None
    salesGrowthRate: Optional[float] = None
    profit: Optional[int] = None
    profitGrowthRate: Optional[float] = None
    income: Optional[int] = None
    divide: Optional[int] = None
    EPS: Optional[int] = None
    PER: Optional[float] = None
    ROE: Optional[float] = None
    ROA: Optional[float] = None
    PBR: Optional[float] = None
    retentionRate: Optional[float] = None
    divideRate: Optional[float] = None
