# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        x,
        draws,
        radar,
        drafts,
        events,
        styles,
        trends,
        account,
        compose,
        credits,
        support,
        api_keys,
        monitors,
        webhooks,
        subscribe,
        extractions,
        integrations,
    )
    from .resources.x.x import XResource, AsyncXResource
    from .resources.draws import DrawsResource, AsyncDrawsResource
    from .resources.radar import RadarResource, AsyncRadarResource
    from .resources.drafts import DraftsResource, AsyncDraftsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.styles import StylesResource, AsyncStylesResource
    from .resources.trends import TrendsResource, AsyncTrendsResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.compose import ComposeResource, AsyncComposeResource
    from .resources.credits import CreditsResource, AsyncCreditsResource
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.monitors import MonitorsResource, AsyncMonitorsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.subscribe import SubscribeResource, AsyncSubscribeResource
    from .resources.extractions import ExtractionsResource, AsyncExtractionsResource
    from .resources.integrations import IntegrationsResource, AsyncIntegrationsResource
    from .resources.support.support import SupportResource, AsyncSupportResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "XTwitterScraper",
    "AsyncXTwitterScraper",
    "Client",
    "AsyncClient",
]


class XTwitterScraper(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous XTwitterScraper client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `X_TWITTER_SCRAPER_API_KEY`
        - `bearer_token` from `X_TWITTER_SCRAPER_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("X_TWITTER_SCRAPER_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("X_TWITTER_SCRAPER_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("X_TWITTER_SCRAPER_BASE_URL")
        if base_url is None:
            base_url = f"https://xquik.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account(self) -> AccountResource:
        """Account info and settings"""
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        """API key management (session auth only)"""
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def subscribe(self) -> SubscribeResource:
        """Subscription, billing, and credits"""
        from .resources.subscribe import SubscribeResource

        return SubscribeResource(self)

    @cached_property
    def compose(self) -> ComposeResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import ComposeResource

        return ComposeResource(self)

    @cached_property
    def drafts(self) -> DraftsResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import DraftsResource

        return DraftsResource(self)

    @cached_property
    def styles(self) -> StylesResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import StylesResource

        return StylesResource(self)

    @cached_property
    def radar(self) -> RadarResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import RadarResource

        return RadarResource(self)

    @cached_property
    def monitors(self) -> MonitorsResource:
        """Real-time X account monitoring"""
        from .resources.monitors import MonitorsResource

        return MonitorsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """Activity events from monitored accounts"""
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def extractions(self) -> ExtractionsResource:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import ExtractionsResource

        return ExtractionsResource(self)

    @cached_property
    def draws(self) -> DrawsResource:
        """Giveaway draws from tweet replies"""
        from .resources.draws import DrawsResource

        return DrawsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def x(self) -> XResource:
        from .resources.x import XResource

        return XResource(self)

    @cached_property
    def trends(self) -> TrendsResource:
        """Trending topics and hashtags by region"""
        from .resources.trends import TrendsResource

        return TrendsResource(self)

    @cached_property
    def support(self) -> SupportResource:
        from .resources.support import SupportResource

        return SupportResource(self)

    @cached_property
    def credits(self) -> CreditsResource:
        """Subscription, billing, and credits"""
        from .resources.credits import CreditsResource

        return CreditsResource(self)

    @cached_property
    def with_raw_response(self) -> XTwitterScraperWithRawResponse:
        return XTwitterScraperWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XTwitterScraperWithStreamedResponse:
        return XTwitterScraperWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
            **(self._oauth_bearer if security.get("oauth_bearer", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-Key": api_key}

    @property
    def _oauth_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-Api-Key") or isinstance(custom_headers.get("X-Api-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncXTwitterScraper(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncXTwitterScraper client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `X_TWITTER_SCRAPER_API_KEY`
        - `bearer_token` from `X_TWITTER_SCRAPER_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("X_TWITTER_SCRAPER_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("X_TWITTER_SCRAPER_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("X_TWITTER_SCRAPER_BASE_URL")
        if base_url is None:
            base_url = f"https://xquik.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account(self) -> AsyncAccountResource:
        """Account info and settings"""
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        """API key management (session auth only)"""
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResource:
        """Subscription, billing, and credits"""
        from .resources.subscribe import AsyncSubscribeResource

        return AsyncSubscribeResource(self)

    @cached_property
    def compose(self) -> AsyncComposeResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import AsyncComposeResource

        return AsyncComposeResource(self)

    @cached_property
    def drafts(self) -> AsyncDraftsResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import AsyncDraftsResource

        return AsyncDraftsResource(self)

    @cached_property
    def styles(self) -> AsyncStylesResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import AsyncStylesResource

        return AsyncStylesResource(self)

    @cached_property
    def radar(self) -> AsyncRadarResource:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import AsyncRadarResource

        return AsyncRadarResource(self)

    @cached_property
    def monitors(self) -> AsyncMonitorsResource:
        """Real-time X account monitoring"""
        from .resources.monitors import AsyncMonitorsResource

        return AsyncMonitorsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Activity events from monitored accounts"""
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def extractions(self) -> AsyncExtractionsResource:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import AsyncExtractionsResource

        return AsyncExtractionsResource(self)

    @cached_property
    def draws(self) -> AsyncDrawsResource:
        """Giveaway draws from tweet replies"""
        from .resources.draws import AsyncDrawsResource

        return AsyncDrawsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def x(self) -> AsyncXResource:
        from .resources.x import AsyncXResource

        return AsyncXResource(self)

    @cached_property
    def trends(self) -> AsyncTrendsResource:
        """Trending topics and hashtags by region"""
        from .resources.trends import AsyncTrendsResource

        return AsyncTrendsResource(self)

    @cached_property
    def support(self) -> AsyncSupportResource:
        from .resources.support import AsyncSupportResource

        return AsyncSupportResource(self)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        """Subscription, billing, and credits"""
        from .resources.credits import AsyncCreditsResource

        return AsyncCreditsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncXTwitterScraperWithRawResponse:
        return AsyncXTwitterScraperWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXTwitterScraperWithStreamedResponse:
        return AsyncXTwitterScraperWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
            **(self._oauth_bearer if security.get("oauth_bearer", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-Key": api_key}

    @property
    def _oauth_bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-Api-Key") or isinstance(custom_headers.get("X-Api-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class XTwitterScraperWithRawResponse:
    _client: XTwitterScraper

    def __init__(self, client: XTwitterScraper) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        """Account info and settings"""
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        """API key management (session auth only)"""
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def subscribe(self) -> subscribe.SubscribeResourceWithRawResponse:
        """Subscription, billing, and credits"""
        from .resources.subscribe import SubscribeResourceWithRawResponse

        return SubscribeResourceWithRawResponse(self._client.subscribe)

    @cached_property
    def compose(self) -> compose.ComposeResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import ComposeResourceWithRawResponse

        return ComposeResourceWithRawResponse(self._client.compose)

    @cached_property
    def drafts(self) -> drafts.DraftsResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import DraftsResourceWithRawResponse

        return DraftsResourceWithRawResponse(self._client.drafts)

    @cached_property
    def styles(self) -> styles.StylesResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import StylesResourceWithRawResponse

        return StylesResourceWithRawResponse(self._client.styles)

    @cached_property
    def radar(self) -> radar.RadarResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import RadarResourceWithRawResponse

        return RadarResourceWithRawResponse(self._client.radar)

    @cached_property
    def monitors(self) -> monitors.MonitorsResourceWithRawResponse:
        """Real-time X account monitoring"""
        from .resources.monitors import MonitorsResourceWithRawResponse

        return MonitorsResourceWithRawResponse(self._client.monitors)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """Activity events from monitored accounts"""
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithRawResponse:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import ExtractionsResourceWithRawResponse

        return ExtractionsResourceWithRawResponse(self._client.extractions)

    @cached_property
    def draws(self) -> draws.DrawsResourceWithRawResponse:
        """Giveaway draws from tweet replies"""
        from .resources.draws import DrawsResourceWithRawResponse

        return DrawsResourceWithRawResponse(self._client.draws)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def x(self) -> x.XResourceWithRawResponse:
        from .resources.x import XResourceWithRawResponse

        return XResourceWithRawResponse(self._client.x)

    @cached_property
    def trends(self) -> trends.TrendsResourceWithRawResponse:
        """Trending topics and hashtags by region"""
        from .resources.trends import TrendsResourceWithRawResponse

        return TrendsResourceWithRawResponse(self._client.trends)

    @cached_property
    def support(self) -> support.SupportResourceWithRawResponse:
        from .resources.support import SupportResourceWithRawResponse

        return SupportResourceWithRawResponse(self._client.support)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithRawResponse:
        """Subscription, billing, and credits"""
        from .resources.credits import CreditsResourceWithRawResponse

        return CreditsResourceWithRawResponse(self._client.credits)


class AsyncXTwitterScraperWithRawResponse:
    _client: AsyncXTwitterScraper

    def __init__(self, client: AsyncXTwitterScraper) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        """Account info and settings"""
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        """API key management (session auth only)"""
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def subscribe(self) -> subscribe.AsyncSubscribeResourceWithRawResponse:
        """Subscription, billing, and credits"""
        from .resources.subscribe import AsyncSubscribeResourceWithRawResponse

        return AsyncSubscribeResourceWithRawResponse(self._client.subscribe)

    @cached_property
    def compose(self) -> compose.AsyncComposeResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import AsyncComposeResourceWithRawResponse

        return AsyncComposeResourceWithRawResponse(self._client.compose)

    @cached_property
    def drafts(self) -> drafts.AsyncDraftsResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import AsyncDraftsResourceWithRawResponse

        return AsyncDraftsResourceWithRawResponse(self._client.drafts)

    @cached_property
    def styles(self) -> styles.AsyncStylesResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import AsyncStylesResourceWithRawResponse

        return AsyncStylesResourceWithRawResponse(self._client.styles)

    @cached_property
    def radar(self) -> radar.AsyncRadarResourceWithRawResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import AsyncRadarResourceWithRawResponse

        return AsyncRadarResourceWithRawResponse(self._client.radar)

    @cached_property
    def monitors(self) -> monitors.AsyncMonitorsResourceWithRawResponse:
        """Real-time X account monitoring"""
        from .resources.monitors import AsyncMonitorsResourceWithRawResponse

        return AsyncMonitorsResourceWithRawResponse(self._client.monitors)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """Activity events from monitored accounts"""
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithRawResponse:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import AsyncExtractionsResourceWithRawResponse

        return AsyncExtractionsResourceWithRawResponse(self._client.extractions)

    @cached_property
    def draws(self) -> draws.AsyncDrawsResourceWithRawResponse:
        """Giveaway draws from tweet replies"""
        from .resources.draws import AsyncDrawsResourceWithRawResponse

        return AsyncDrawsResourceWithRawResponse(self._client.draws)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def x(self) -> x.AsyncXResourceWithRawResponse:
        from .resources.x import AsyncXResourceWithRawResponse

        return AsyncXResourceWithRawResponse(self._client.x)

    @cached_property
    def trends(self) -> trends.AsyncTrendsResourceWithRawResponse:
        """Trending topics and hashtags by region"""
        from .resources.trends import AsyncTrendsResourceWithRawResponse

        return AsyncTrendsResourceWithRawResponse(self._client.trends)

    @cached_property
    def support(self) -> support.AsyncSupportResourceWithRawResponse:
        from .resources.support import AsyncSupportResourceWithRawResponse

        return AsyncSupportResourceWithRawResponse(self._client.support)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithRawResponse:
        """Subscription, billing, and credits"""
        from .resources.credits import AsyncCreditsResourceWithRawResponse

        return AsyncCreditsResourceWithRawResponse(self._client.credits)


class XTwitterScraperWithStreamedResponse:
    _client: XTwitterScraper

    def __init__(self, client: XTwitterScraper) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        """Account info and settings"""
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        """API key management (session auth only)"""
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def subscribe(self) -> subscribe.SubscribeResourceWithStreamingResponse:
        """Subscription, billing, and credits"""
        from .resources.subscribe import SubscribeResourceWithStreamingResponse

        return SubscribeResourceWithStreamingResponse(self._client.subscribe)

    @cached_property
    def compose(self) -> compose.ComposeResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import ComposeResourceWithStreamingResponse

        return ComposeResourceWithStreamingResponse(self._client.compose)

    @cached_property
    def drafts(self) -> drafts.DraftsResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import DraftsResourceWithStreamingResponse

        return DraftsResourceWithStreamingResponse(self._client.drafts)

    @cached_property
    def styles(self) -> styles.StylesResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import StylesResourceWithStreamingResponse

        return StylesResourceWithStreamingResponse(self._client.styles)

    @cached_property
    def radar(self) -> radar.RadarResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import RadarResourceWithStreamingResponse

        return RadarResourceWithStreamingResponse(self._client.radar)

    @cached_property
    def monitors(self) -> monitors.MonitorsResourceWithStreamingResponse:
        """Real-time X account monitoring"""
        from .resources.monitors import MonitorsResourceWithStreamingResponse

        return MonitorsResourceWithStreamingResponse(self._client.monitors)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """Activity events from monitored accounts"""
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithStreamingResponse:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import ExtractionsResourceWithStreamingResponse

        return ExtractionsResourceWithStreamingResponse(self._client.extractions)

    @cached_property
    def draws(self) -> draws.DrawsResourceWithStreamingResponse:
        """Giveaway draws from tweet replies"""
        from .resources.draws import DrawsResourceWithStreamingResponse

        return DrawsResourceWithStreamingResponse(self._client.draws)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def x(self) -> x.XResourceWithStreamingResponse:
        from .resources.x import XResourceWithStreamingResponse

        return XResourceWithStreamingResponse(self._client.x)

    @cached_property
    def trends(self) -> trends.TrendsResourceWithStreamingResponse:
        """Trending topics and hashtags by region"""
        from .resources.trends import TrendsResourceWithStreamingResponse

        return TrendsResourceWithStreamingResponse(self._client.trends)

    @cached_property
    def support(self) -> support.SupportResourceWithStreamingResponse:
        from .resources.support import SupportResourceWithStreamingResponse

        return SupportResourceWithStreamingResponse(self._client.support)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithStreamingResponse:
        """Subscription, billing, and credits"""
        from .resources.credits import CreditsResourceWithStreamingResponse

        return CreditsResourceWithStreamingResponse(self._client.credits)


class AsyncXTwitterScraperWithStreamedResponse:
    _client: AsyncXTwitterScraper

    def __init__(self, client: AsyncXTwitterScraper) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        """Account info and settings"""
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        """API key management (session auth only)"""
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def subscribe(self) -> subscribe.AsyncSubscribeResourceWithStreamingResponse:
        """Subscription, billing, and credits"""
        from .resources.subscribe import AsyncSubscribeResourceWithStreamingResponse

        return AsyncSubscribeResourceWithStreamingResponse(self._client.subscribe)

    @cached_property
    def compose(self) -> compose.AsyncComposeResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.compose import AsyncComposeResourceWithStreamingResponse

        return AsyncComposeResourceWithStreamingResponse(self._client.compose)

    @cached_property
    def drafts(self) -> drafts.AsyncDraftsResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.drafts import AsyncDraftsResourceWithStreamingResponse

        return AsyncDraftsResourceWithStreamingResponse(self._client.drafts)

    @cached_property
    def styles(self) -> styles.AsyncStylesResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.styles import AsyncStylesResourceWithStreamingResponse

        return AsyncStylesResourceWithStreamingResponse(self._client.styles)

    @cached_property
    def radar(self) -> radar.AsyncRadarResourceWithStreamingResponse:
        """AI tweet composition, drafts, writing styles, and radar"""
        from .resources.radar import AsyncRadarResourceWithStreamingResponse

        return AsyncRadarResourceWithStreamingResponse(self._client.radar)

    @cached_property
    def monitors(self) -> monitors.AsyncMonitorsResourceWithStreamingResponse:
        """Real-time X account monitoring"""
        from .resources.monitors import AsyncMonitorsResourceWithStreamingResponse

        return AsyncMonitorsResourceWithStreamingResponse(self._client.monitors)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """Activity events from monitored accounts"""
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithStreamingResponse:
        """Bulk data extraction (20 tool types)"""
        from .resources.extractions import AsyncExtractionsResourceWithStreamingResponse

        return AsyncExtractionsResourceWithStreamingResponse(self._client.extractions)

    @cached_property
    def draws(self) -> draws.AsyncDrawsResourceWithStreamingResponse:
        """Giveaway draws from tweet replies"""
        from .resources.draws import AsyncDrawsResourceWithStreamingResponse

        return AsyncDrawsResourceWithStreamingResponse(self._client.draws)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Webhook endpoint management and delivery"""
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        """Push notification integrations (Telegram)"""
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def x(self) -> x.AsyncXResourceWithStreamingResponse:
        from .resources.x import AsyncXResourceWithStreamingResponse

        return AsyncXResourceWithStreamingResponse(self._client.x)

    @cached_property
    def trends(self) -> trends.AsyncTrendsResourceWithStreamingResponse:
        """Trending topics and hashtags by region"""
        from .resources.trends import AsyncTrendsResourceWithStreamingResponse

        return AsyncTrendsResourceWithStreamingResponse(self._client.trends)

    @cached_property
    def support(self) -> support.AsyncSupportResourceWithStreamingResponse:
        from .resources.support import AsyncSupportResourceWithStreamingResponse

        return AsyncSupportResourceWithStreamingResponse(self._client.support)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithStreamingResponse:
        """Subscription, billing, and credits"""
        from .resources.credits import AsyncCreditsResourceWithStreamingResponse

        return AsyncCreditsResourceWithStreamingResponse(self._client.credits)


Client = XTwitterScraper

AsyncClient = AsyncXTwitterScraper
