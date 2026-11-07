# X API & Twitter API Python SDK by Xquik

Use this Twitter API Python SDK by Xquik to read tweets as Pydantic models.
Sync & async clients share every method.
Public reads need no X developer account.

Xquik is the world's fastest and cheapest X (Twitter) scraper service with the most complete X (Twitter) data.
Most other Apify Actors charge before filtering or deduplication.
Xquik charges only for delivered, unique, filter-matching results and never pads rows.
Xquik is independent and not affiliated with X Corp.

<!-- trust:win:start -->

The Xquik REST API read 45 tweets per second on 2026-10-15. That cost $0.15 per 1,000. The fastest of 4 rival Actors read 12.5 per second. The cheapest cost $0.173 per 1,000. [Compare each run](https://xquik.com/benchmarks#benchmark-x-tweet-scraper).

<!-- trust:win:end -->

## Install the Twitter API for Python

The SDK requires Python 3.10 or later.

```sh
pip install x_twitter_scraper
```

## Search tweets with the Python Twitter API

Set `X_TWITTER_SCRAPER_API_KEY`, then run this search.

```python
import os
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper(
    api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional. The client reads this variable.
)

response = client.x.tweets.search(
    q="from:elonmusk",
    limit=10,
)
for tweet in response.tweets:
    print(tweet.id, tweet.text)
```

Next, read the [Python SDK guide](https://docs.xquik.com/sdks/python), [API map](api.md) or [REST reference](https://docs.xquik.com/api-reference/overview).

<!-- trust:start -->

## Benchmarks & usage

[![x-twitter-scraper downloads on PyPI](https://img.shields.io/endpoint?url=https%3A%2F%2Fxquik.com%2Fbadges%2Fpypi-x-twitter-scraper.json)](https://pypistats.org/packages/x-twitter-scraper)
[![X (Twitter) API p99 server read time](https://img.shields.io/endpoint?url=https%3A%2F%2Fxquik.com%2Fbadges%2Frest-p99.json)](https://xquik.com/benchmarks#speed)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13738/badge)](https://www.bestpractices.dev/projects/13738)

- 4,400+ downloads of x-twitter-scraper on PyPI ([source](https://pypistats.org/packages/x-twitter-scraper)) <!-- trust:pypi-x-twitter-scraper 4460 -->
- 5.8 s p99 REST server read time over 7 days, failures included ([source](https://xquik.com/benchmarks#speed)) <!-- trust:rest-p99 5793 -->
- This repo meets the OpenSSF Best Practices passing criteria ([source](https://www.bestpractices.dev/projects/13738)) <!-- trust:openssf-x-twitter-scraper-python 1 -->

Checked on 2026-11-07. See each number with its date & source on [xquik.com/benchmarks](https://xquik.com/benchmarks) or as [JSON](https://xquik.com/trust.json).

<!-- trust:end -->

## Move from Tweepy

Tweepy calls the official X API, which needs a developer account & bearer token.
This SDK reads public X data with an Xquik API key.
This call replaces a Tweepy `search_recent_tweets` call.

```python
# Tweepy: client.search_recent_tweets(query="from:NASA", max_results=10)
response = client.x.tweets.search(q="from:NASA", limit=10)
```

## Replace snscrape for Twitter search

Code built on snscrape's `TwitterSearchScraper` maps to 1 SDK call.
The SDK takes the same X search operators & returns typed tweets.

```python
# snscrape: TwitterSearchScraper("from:NASA since:2026-10-01").get_items()
response = client.x.tweets.search(q="from:NASA since:2026-10-01", limit=25)
for tweet in response.tweets:
    print(tweet.id, tweet.text)
```

## Common Twitter & X tasks

| Task | REST route | Usage |
| --- | --- | --- |
| Search tweets without the X API | `GET /x/tweets/search` | Use keyword or advanced operator queries. |
| Read an X profile timeline | `GET /x/users/{id}/tweets` | Pass the cursor to read the next page. |
| Scrape Twitter followers | `GET /x/users/{id}/followers` | Use an extraction for complete datasets. |
| Scrape following accounts | `GET /x/users/{id}/following` | Use an extraction for complete datasets. |
| Read a home timeline | `GET /x/timeline` | Connect an X account first. |
| Export large X datasets | `POST /extractions` | Poll status, then download results. |
| Run giveaway draws | `POST /draws` | Pick winners from post replies. |
| Download or upload media | `/x/media/*` | Use typed file helpers. |
| Monitor an account | `POST /monitors` | Deliver events through HMAC webhooks. |
| Post or reply | `POST /x/tweets` | Confirm the account and payload. |

## AI agent workflows with MCP

Use the typed REST SDK in application code. Add `https://xquik.com/mcp` to MCP clients.
Follow the [MCP guide](https://docs.xquik.com/mcp/overview) for current authentication support.

## Async usage

Import `AsyncXTwitterScraper` and await each API call.

```python
import os
import asyncio
from x_twitter_scraper import AsyncXTwitterScraper

client = AsyncXTwitterScraper(
    api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional. The client reads this variable.
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

The async client uses `httpx`. Install `aiohttp` for an alternative backend.

```sh
pip install x_twitter_scraper[aiohttp]
```

Select it with `http_client=DefaultAioHttpClient()`.

```python
import os
import asyncio
from x_twitter_scraper import DefaultAioHttpClient
from x_twitter_scraper import AsyncXTwitterScraper


async def main() -> None:
    async with AsyncXTwitterScraper(
        api_key=os.environ.get("X_TWITTER_SCRAPER_API_KEY"),  # Optional. The client reads this variable.
        http_client=DefaultAioHttpClient(),
    ) as client:
        response = await client.x.tweets.search(
            q="from:elonmusk",
            limit=10,
        )


asyncio.run(main())
```

## Using types

Nested request parameters use [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).
Responses use [Pydantic models](https://docs.pydantic.dev) with these helpers.

- Serialize to JSON with `model.to_json()`.
- Convert to a dictionary with `model.to_dict()`.

Set `python.analysis.typeCheckingMode` to `basic` in VS Code to catch type errors.

## File uploads

Pass uploads as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), or `(filename, contents, media_type)`.

```python
from pathlib import Path
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper()

client.x.media.upload(
    account="@elonmusk",
    file=Path("/path/to/file"),
    idempotency_key="upload-2026-10-15",
)
```

The async client uses the same interface and reads `PathLike` content asynchronously.

## Handling errors

Connection failures raise an `APIConnectionError` subclass.
Non-2xx responses raise an `APIStatusError` subclass with `status_code` and `response`.
Every SDK error inherits from `APIError`.

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

The SDK uses these error classes.

| Status code | Error type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 409         | `ConflictError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

The SDK retries connection errors and HTTP 408, 409, 429, and 5xx responses.
It uses exponential backoff and attempts 2 retries by default.

Set `max_retries` to change or disable retries.
Set it on the client, or on 1 request through `with_options`.

```python
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper(
    max_retries=0,
)

client.with_options(max_retries=5).x.tweets.search(
    q="from:elonmusk",
    limit=10,
)
```

### Timeouts

Requests time out after 1 minute, and connections after 5 seconds.
Set a float or [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) through `timeout`.
Set it on the client, or on 1 request through `with_options`.

```python
import httpx
from x_twitter_scraper import XTwitterScraper

client = XTwitterScraper(
    timeout=20.0,
)

client = XTwitterScraper(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

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

### Distinguishing `None`, `null` & missing fields

Both missing and explicit `null` response fields map to `None`.
Check `.model_fields_set` to distinguish them.

```py
if response.my_field is None:
    if "my_field" not in response.model_fields_set:
        print('The response omitted "my_field".')
    else:
        print('The response set "my_field" to null.')
```

### Accessing raw response data

Prefix a method with `.with_raw_response.` to access the raw response.

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

Sync methods return [`APIResponse`](https://github.com/Xquik-dev/x-twitter-scraper-python/blob/main/src/x_twitter_scraper/_response.py).
Async methods return `AsyncAPIResponse` with awaitable content readers.

#### `.with_streaming_response`

The raw-response interface reads the complete body when you make the request.
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

### Making custom or undocumented requests

The SDK types every documented endpoint, parameter, and response property.
Use its lower-level methods for undocumented API features.

#### Undocumented endpoints

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

#### Undocumented request parameters

Pass extra values through `extra_query`, `extra_body`, or `extra_headers`.

#### Undocumented response properties

Read an extra field through `response.unknown_prop`.
Use [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) to get every extra field as a dictionary.

### Configuring the HTTP client

Replace the [httpx client](https://www.python-httpx.org/api/#client) to configure these options.

- [Proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Other [advanced](https://www.python-httpx.org/advanced/clients/) client features

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

Use `with_options()` to replace it for one request.

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

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

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) with these exceptions.

1. Static type changes that preserve runtime behavior.
2. Changes to undocumented internals that stay public.
3. Changes unlikely to affect normal use.

Open an [issue](https://github.com/Xquik-dev/x-twitter-scraper-python/issues) with questions, bugs or suggestions.

### Determining the installed version

If new features are missing, Python may still load an older package.
Check the runtime version.

```py
import x_twitter_scraper

print(x_twitter_scraper.__version__)
```

## Questions

### Do I need an X developer account?

No. Public reads need only an Xquik API key.
Private reads & X account actions need a connected X account.

### Is this the official X API?

No. Xquik runs its own REST API. This SDK calls that API, not the official X API.

## More Xquik tools

- [X (Twitter) scraper API & Twitter MCP server](https://github.com/Xquik-dev/x-twitter-scraper) with REST, MCP & Skill setup.
- Twitter API SDKs for [TypeScript](https://github.com/Xquik-dev/x-twitter-scraper-typescript), [Go](https://github.com/Xquik-dev/x-twitter-scraper-go), [Ruby](https://github.com/Xquik-dev/x-twitter-scraper-ruby) & [Java](https://github.com/Xquik-dev/x-twitter-scraper-java).
- More Twitter API SDKs for [Kotlin](https://github.com/Xquik-dev/x-twitter-scraper-kotlin), [C#](https://github.com/Xquik-dev/x-twitter-scraper-csharp) & [PHP](https://github.com/Xquik-dev/x-twitter-scraper-php).
- [Twitter CLI & X CLI](https://github.com/Xquik-dev/x-twitter-scraper-cli) for terminal workflows.
- [Twitter advanced search operators](https://github.com/Xquik-dev/x-twitter-advanced-search) with tested examples.
- Twitter agent plugins for [OpenClaw](https://github.com/Xquik-dev/tweetclaw) & [Hermes Agent](https://github.com/Xquik-dev/hermes-tweet).
- Twitter integrations for [n8n](https://github.com/Xquik-dev/n8n-nodes-xquik), [Prefect](https://github.com/Xquik-dev/prefect-xquik), [Haystack](https://github.com/Xquik-dev/xquik-haystack) & [Paperclip](https://github.com/Xquik-dev/paperclip-plugin-xquik).
- More Twitter integrations for [Terraform](https://github.com/Xquik-dev/terraform-provider-x-twitter-scraper), [Convex](https://github.com/Xquik-dev/xquik-convex), [Supabase](https://github.com/Xquik-dev/xquik-supabase) & [Strapi](https://github.com/Xquik-dev/strapi-plugin-xquik).
- Twitter MCP for [AI agents](https://github.com/Xquik-dev/xquik-mcp), [VS Code](https://github.com/Xquik-dev/xquik-vscode) & [Raycast](https://github.com/Xquik-dev/xquik-raycast).
- [Xquik X API & Twitter scraper](https://xquik.com), [Twitter API docs](https://docs.xquik.com/api-reference/overview) & [docs source](https://github.com/Xquik-dev/xquik-docs).

## Help & contributing

- Report vulnerabilities through the [security policy](SECURITY.md).
- Ask usage questions through the [organization support policy](https://github.com/Xquik-dev/.github/blob/main/SUPPORT.md).
- Read the [contribution guide](CONTRIBUTING.md) & [governance policy](GOVERNANCE.md).
- Read the [OpenSSF evidence](OPENSSF.md) & [citation metadata](CITATION.cff).

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
