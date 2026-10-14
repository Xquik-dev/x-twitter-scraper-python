# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from .support import (
    SupportResource,
    AsyncSupportResource,
    SupportResourceWithRawResponse,
    AsyncSupportResourceWithRawResponse,
    SupportResourceWithStreamingResponse,
    AsyncSupportResourceWithStreamingResponse,
)
from .tickets import (
    TicketsResource,
    AsyncTicketsResource,
    TicketsResourceWithRawResponse,
    AsyncTicketsResourceWithRawResponse,
    TicketsResourceWithStreamingResponse,
    AsyncTicketsResourceWithStreamingResponse,
)
from .attachments import (
    AttachmentsResource,
    AsyncAttachmentsResource,
    AttachmentsResourceWithRawResponse,
    AsyncAttachmentsResourceWithRawResponse,
    AttachmentsResourceWithStreamingResponse,
    AsyncAttachmentsResourceWithStreamingResponse,
)

__all__ = [
    "AttachmentsResource",
    "AsyncAttachmentsResource",
    "AttachmentsResourceWithRawResponse",
    "AsyncAttachmentsResourceWithRawResponse",
    "AttachmentsResourceWithStreamingResponse",
    "AsyncAttachmentsResourceWithStreamingResponse",
    "TicketsResource",
    "AsyncTicketsResource",
    "TicketsResourceWithRawResponse",
    "AsyncTicketsResourceWithRawResponse",
    "TicketsResourceWithStreamingResponse",
    "AsyncTicketsResourceWithStreamingResponse",
    "SupportResource",
    "AsyncSupportResource",
    "SupportResourceWithRawResponse",
    "AsyncSupportResourceWithRawResponse",
    "SupportResourceWithStreamingResponse",
    "AsyncSupportResourceWithStreamingResponse",
]
