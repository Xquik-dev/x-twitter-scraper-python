from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractionCancelResponse"]


class ExtractionCancelResponse(BaseModel):
    id: str

    status: Literal["canceled"]
