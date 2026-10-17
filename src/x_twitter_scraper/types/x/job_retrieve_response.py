# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from .job import Job, Account as JobAccount, Company as JobCompany
from ..._models import BaseModel

__all__ = ["JobRetrieveResponse", "Job", "JobAccount", "JobCompany"]


class JobRetrieveResponse(BaseModel):
    job: Job
    """Public X job listing.

    A search returns the fields down to the salary, plus company & account. A lookup
    adds work type, seniority, function, team & descriptions. A field X leaves empty
    is left out.
    """
