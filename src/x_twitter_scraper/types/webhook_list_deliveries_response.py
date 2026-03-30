# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .delivery import Delivery

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
    deliveries: List[Delivery]
