import pydantic
from typing import Optional


class StockData(pydantic.BaseModel):

    name: str
    volume: Optional[int] = None  # 거래량
    price: Optional[int] = None  # 현재가
    open: Optional[int] = None  # 시가
    close: Optional[int] = None  # 종가
    high: Optional[int] = None  # 고가
    low: Optional[int] = None  # 저가
    foreignRate: Optional[float] = None  # 외국인비율
    marketCap: Optional[int] = None  # 시가총액
    asset: Optional[int] = None  # 자산총계
    liability: Optional[int] = None  # 부채총계
    revenue: Optional[int] = None  # 매출액
    revenueGrowthRate: Optional[float] = None  # 매출액증가율
    income: Optional[int] = None  # 영업이익
    incomeGrowthRate: Optional[float] = None  # 영업이익증가율
    profit: Optional[int] = None  # 당기순이익
    divide: Optional[int] = None  # 배당금
    EPS: Optional[int] = None  # 주당순이익
    PER: Optional[float] = None
    ROE: Optional[float] = None
    ROA: Optional[float] = None
    PBR: Optional[float] = None
    retentionRate: Optional[float] = None  # 유보율
    divideRate: Optional[float] = None  # 배당수익률
