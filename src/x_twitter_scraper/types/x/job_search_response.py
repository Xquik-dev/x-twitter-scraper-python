# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from .job import Job, Account as JobAccount, Company as JobCompany
from ..._models import BaseModel

__all__ = ["JobSearchResponse", "Job", "JobAccount", "JobCompany"]


class JobSearchResponse(BaseModel):
    """One page of job listings.

    Follow next_cursor while the response reports more pages.
    """

    has_next_page: bool

    jobs: List[Job]

    next_cursor: str
