# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JobSearchResponse", "Job", "JobAccount", "JobCompany"]


class JobAccount(BaseModel):
    """The X account that posted a job.

    A job has none when X imported it from a job board or no longer shows the account.
    """

    id: str
    """X user ID of the account."""

    verified: bool
    """Whether X shows a verification badge on the account."""

    description: Optional[str] = None
    """Bio of the account. A job lookup returns it."""

    name: Optional[str] = None
    """Display name of the account that posted the job."""

    profile_image_shape: Optional[str] = FieldInfo(alias="profileImageShape", default=None)
    """Avatar shape, such as Circle or Square."""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Avatar URL of the account that posted the job."""

    username: Optional[str] = None
    """Handle without @."""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Badge type, such as Business or Government."""


class JobCompany(BaseModel):
    """The company profile of a job X imported from a job board."""

    id: str
    """X company profile ID."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Company logo URL."""

    name: Optional[str] = None
    """Company name."""


class Job(BaseModel):
    """Public X job listing.

    A search returns the fields down to the salary, plus company & account. A lookup adds work type, seniority, function, team & descriptions. A field X leaves empty is left out.
    """

    id: str
    """Job ID."""

    url: str
    """The job page on X."""

    account: Optional[JobAccount] = None
    """The X account that posted a job.

    A job has none when X imported it from a job board or no longer shows the
    account.
    """

    apply_url: Optional[str] = FieldInfo(alias="applyUrl", default=None)
    """Where applicants apply, off X."""

    company: Optional[JobCompany] = None
    """The company profile of a job X imported from a job board."""

    description: Optional[str] = None
    """Full description as plain text, 1 line per paragraph."""

    description_markdown: Optional[str] = FieldInfo(alias="descriptionMarkdown", default=None)
    """Full description as Markdown, with headings, lists, links, bold & italics."""

    employment_type: Optional[str] = FieldInfo(alias="employmentType", default=None)
    """Contract type (full_time, full_time_contract, part_time or contract_to_hire)."""

    featured: Optional[bool] = None
    """Whether X features the job."""

    formatted_salary: Optional[str] = FieldInfo(alias="formattedSalary", default=None)
    """Salary as X shows it."""

    job_function: Optional[str] = FieldInfo(alias="jobFunction", default=None)
    """Job function, such as software_engineering."""

    location: Optional[str] = None
    """Location as the employer wrote it."""

    location_type: Optional[str] = FieldInfo(alias="locationType", default=None)
    """Where the work happens (onsite, remote or hybrid)."""

    posted_at: Optional[datetime] = FieldInfo(alias="postedAt", default=None)
    """When the employer posted the job."""

    salary_currency_code: Optional[str] = FieldInfo(alias="salaryCurrencyCode", default=None)
    """ISO 4217 currency code of the salary."""

    salary_interval: Optional[str] = FieldInfo(alias="salaryInterval", default=None)
    """Pay period of the salary (annually or hourly)."""

    salary_max: Optional[float] = FieldInfo(alias="salaryMax", default=None)
    """Highest salary, in salaryCurrencyCode per salaryInterval."""

    salary_min: Optional[float] = FieldInfo(alias="salaryMin", default=None)
    """Lowest salary, in salaryCurrencyCode per salaryInterval."""

    seniority_level: Optional[str] = FieldInfo(alias="seniorityLevel", default=None)
    """
    Seniority (intern, entry_level, junior, mid_level, senior, lead, manager or
    executive).
    """

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)
    """Short summary of the job, as plain text."""

    team: Optional[str] = None
    """Team inside the company."""

    title: Optional[str] = None
    """Job title."""


class JobSearchResponse(BaseModel):
    """One page of job listings.

    Follow next_cursor while the response reports more pages.
    """

    has_next_page: bool

    jobs: List[Job]

    next_cursor: str
