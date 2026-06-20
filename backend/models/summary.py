from pydantic import BaseModel


class Summary(BaseModel):
    title: str
    url: str
    summary: str