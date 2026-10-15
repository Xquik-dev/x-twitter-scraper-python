# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import httpx

DEFAULT_BASE_URL = "https://xquik.com/api/v1"

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "____stainless_override_cast_to"

DEFAULT_TIMEOUT = httpx.Timeout(timeout=60, connect=5.0)
DEFAULT_MAX_RETRIES = 2
DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
