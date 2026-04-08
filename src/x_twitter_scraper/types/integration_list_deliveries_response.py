# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .integration_delivery import IntegrationDelivery

__all__ = ["IntegrationListDeliveriesResponse"]


class IntegrationListDeliveriesResponse(BaseModel):
    deliveries: List[IntegrationDelivery]
