# Xquik Python SDK: Twitter Search, Followers & X Automation

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13738/badge)](https://www.bestpractices.dev/projects/13738)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/x_twitter_scraper.svg?label=pypi%20(stable))](https://pypi.org/project/x_twitter_scraper/)

Use the Xquik Python SDK for Twitter search, timelines, profiles & followers.
Manage media, webhooks & X automation through documented Xquik REST routes.

[Python SDK Guide](https://docs.xquik.com/sdks/python) | [API Map](api.md) | [REST API](https://docs.xquik.com/api-reference/overview) | [Webhooks](https://docs.xquik.com/api-reference/webhooks/create) | [MCP Guide](https://docs.xquik.com/mcp/overview)

[Stainless](https://www.stainless.com/) generates this SDK.

## Common Twitter & X Tasks

| Task | REST Route | Usage |
| --- | --- | --- |
| Search tweets without the X API | `GET /x/tweets/search` | Use keyword or advanced operator queries. |
| Read an X profile timeline | `GET /x/users/{id}/tweets` | Paginate bounded results. |
| Scrape Twitter followers | `GET /x/users/{id}/followers` | Use an extraction for complete datasets. |
| Scrape following accounts | `GET /x/users/{id}/following` | Use an extraction for complete datasets. |
| Read a home timeline | `GET /x/timeline` | Approve this private read. |
| Export large X datasets | `POST /extractions` | Poll status, then download results. |
| Run giveaway draws | `POST /draws` | Pick winners from post replies. |
| Download or upload media | `/x/media/*` | Use typed file helpers. |
| Monitor an account | `POST /monitors` | Deliver events through HMAC webhooks. |
| Post or reply | `POST /x/tweets` | Confirm the account and payload. |

## AI Agent Workflows With MCP

Use the typed REST SDK in application code. Add `https://xquik.com/mcp` to MCP clients.
Follow the [MCP guide](https://docs.xquik.com/mcp/overview) for current authentication support.

## Package & Registry Trust

- Package: [PyPI `x_twitter_scraper`](https://pypi.org/project/x_twitter_scraper/)
- Source: [Xquik-dev/x-twitter-scraper-python](https://github.com/Xquik-dev/x-twitter-scraper-python)
- License: Apache-2.0
- Citation metadata: [CITATION.cff](CITATION.cff)
- Security policy: [SECURITY.md](SECURITY.md)

## Installation

```sh
pip install x_twitter_scraper
```

## Usage

See [api.md](api.md) for the complete API.

```python
import os
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper(
    api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional; the client reads this variable.
)

response = client.x.tweets.search(
    q="from:elonmusk",
    limit=10,
)
```

Pass `api_key` directly or load `X_TWITTER_SCRAPER_API_KEY` with
[python-dotenv](https://pypi.org/project/python-dotenv/). Keep credentials out of source control.

## Async Usage

Import `AsyncXTwitterScraper` and await each API call:

```python
import os
import asyncio
from x_twitter_scraper import AsyncXTwitterScraper

client = AsyncXTwitterScraper(
    api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional; the client reads this variable.
)


async def main() -> None:
    response = await client.x.tweets.search(
        q="from:elonmusk",
        limit=10,
    )


asyncio.run(main())
```

Both clients expose the same resources and methods.

### With aiohttp

The async client uses `httpx`. Install `aiohttp` for an alternative backend:

```sh
pip install x_twitter_scraper[aiohttp]
```

Select it with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from x_twitter_scraper import DefaultAioHttpClient
from x_twitter_scraper import AsyncXTwitterScraper


async def main() -> None:
    async with AsyncXTwitterScraper(
        api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional; the client reads this variable.
        http_client=DefaultAioHttpClient(),
    ) as client:
        response = await client.x.tweets.search(
            q="from:elonmusk",
            limit=10,
        )


asyncio.run(main())
```

## Using Types

Nested request parameters use [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).
Responses use [Pydantic models](https://docs.pydantic.dev) with these helpers:

- Serialize to JSON with `model.to_json()`.
- Convert to a dictionary with `model.to_dict()`.

Set `python.analysis.typeCheckingMode` to `basic` in VS Code to catch type errors.

## File Uploads

Pass uploads as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), or `(filename, contents, media_type)`.

```python
from pathlib import Path
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper()

client.x.media.upload(
    account="@elonmusk",
    file=Path("/path/to/file"),
)
```

The async client uses the same interface and reads `PathLike` content asynchronously.

## Handling Errors

Connection failures raise an `x_twitter_scraper.APIConnectionError` subclass.
Non-2xx responses raise an `APIStatusError` subclass with `status_code` and `response`.
Every SDK error inherits from `x_twitter_scraper.APIError`.

```python
import x_twitter_scraper
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper()

try:
    client.x.tweets.search(
        q="from:elonmusk",
        limit=10,
    )
except x_twitter_scraper.APIConnectionError as e:
    print("Could not reach the server. Check the connection.")
    print(e.__cause__)  # Underlying httpx exception.
except x_twitter_scraper.RateLimitError as e:
    print("Rate limited. Retry later.")
except x_twitter_scraper.APIStatusError as e:
    print("Server returned a non-2xx status.")
    print(e.status_code)
    print(e.response)
```

The SDK uses these error classes:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

The SDK retries connection errors and HTTP 408, 409, 429, and 5xx responses.
It uses exponential backoff and attempts 2 retries by default.

Set `max_retries` to change or disable retries:

```python
from x_twitter_scraper import XTwitterScraper

# Set the client default:
client = XTwitterScraper(
    max_retries=0,
)

# Override one request:
client.with_options(max_retries=5).x.tweets.search(
    q="from:elonmusk",
    limit=10,
)
```

### Timeouts

Requests time out after 1 minute.
Set a float or [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) through `timeout`:

```python
from x_twitter_scraper import XTwitterScraper

# Set the client default:
client = XTwitterScraper(
    # 20 seconds; default: 1 minute.
    timeout=20.0,
)

# Set granular limits:
client = XTwitterScraper(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).x.tweets.search(
    q="from:elonmusk",
    limit=10,
)
```

Timeouts raise `APITimeoutError`.

Timed-out requests follow the [default retry policy](#retries).

## Advanced

### Logging

The SDK uses Python's [`logging`](https://docs.python.org/3/library/logging.html) module.
Set `X_TWITTER_SCRAPER_LOG` to `info` to enable logs.

```shell
$ export X_TWITTER_SCRAPER_LOG=info
```

Use `debug` for request and response details.

### Distinguishing `None`, `null` & Missing Fields

Both missing and explicit `null` response fields map to `None`.
Check `.model_fields_set` to distinguish them:

```py
if response.my_field is None:
    if "my_field" not in response.model_fields_set:
        print('The response omitted "my_field".')
    else:
        print('The response set "my_field" to null.')
```

### Accessing Raw Response Data

Prefix a method with `.with_raw_response.` to access the raw response:

```py
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper()
response = client.x.tweets.with_raw_response.search(
    q="from:elonmusk",
    limit=10,
)
print(response.headers.get("X-My-Header"))

tweet = response.parse()  # Parse the regular x.tweets.search() result.
print(tweet.has_next_page)
```

Sync methods return [`APIResponse`](https://github.com/Xquik-dev/x-twitter-scraper-python/tree/main/src/x_twitter_scraper/_response.py).
Async methods return `AsyncAPIResponse` with awaitable content readers.

#### `.with_streaming_response`

The raw-response interface reads the complete body immediately.
Use `.with_streaming_response` and a context manager to read it on demand.
Call `.read()`, `.text()`, `.json()`, an iterator, or `.parse()`.
The async client provides async versions of these methods.

```python
with client.x.tweets.with_streaming_response.search(
    q="from:elonmusk",
    limit=10,
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager always closes the response.

### Making Custom or Undocumented Requests

The SDK types every documented endpoint, parameter, and response property.
Use its lower-level methods for undocumented API features.

#### Undocumented Endpoints

Use `client.get`, `client.post`, or another HTTP method for undocumented endpoints.
Client options, including retries, apply to these requests.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented Request Parameters

Pass extra values through `extra_query`, `extra_body`, or `extra_headers`.

#### Undocumented Response Properties

Read an extra field through `response.unknown_prop`.
Use [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) to get every extra field as a dictionary.

### Configuring the HTTP Client

Replace the [httpx client](https://www.python-httpx.org/api/#client) to configure:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from x_twitter_scraper import XTwitterScraper, DefaultHttpxClient

client = XTwitterScraper(
    # Or use the `X_TWITTER_SCRAPER_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

Use `with_options()` to replace it for one request:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP Resources

Garbage collection closes the client's HTTP connections.
Call `.close()` or use a context manager to close them earlier.

```py
from x_twitter_scraper import XTwitterScraper

with XTwitterScraper() as client:
    # Make requests here.
    ...

# The HTTP client is closed.
```

## Versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) with these exceptions:

1. Static type changes that preserve runtime behavior.
2. Changes to undocumented internals that remain technically public.
3. Changes unlikely to affect normal use.

Open an [issue](https://www.github.com/Xquik-dev/x-twitter-scraper-python/issues) with questions, bugs, or suggestions.

### Determining the Installed Version

If new features are missing, Python may still load an older package.
Check the runtime version:

```py
import x_twitter_scraper

print(x_twitter_scraper.__version__)
```

## Requirements

Python 3.10 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
