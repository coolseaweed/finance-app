import pydantic


class DummyResponse(pydantic.BaseModel):
    status: str
    data_str: str
    data_int: int
    data_float: float
