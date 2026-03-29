# Account

Types:

```python
from x_twitter_scraper.types import (
    AccountRetrieveResponse,
    AccountSetXUsernameResponse,
    AccountUpdateLocaleResponse,
)
```

Methods:

- <code title="get /account">client.account.<a href="./src/x_twitter_scraper/resources/account.py">retrieve</a>() -> <a href="./src/x_twitter_scraper/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="put /account/x-identity">client.account.<a href="./src/x_twitter_scraper/resources/account.py">set_x_username</a>(\*\*<a href="src/x_twitter_scraper/types/account_set_x_username_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/account_set_x_username_response.py">AccountSetXUsernameResponse</a></code>
- <code title="patch /account">client.account.<a href="./src/x_twitter_scraper/resources/account.py">update_locale</a>(\*\*<a href="src/x_twitter_scraper/types/account_update_locale_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/account_update_locale_response.py">AccountUpdateLocaleResponse</a></code>

# APIKeys

Types:

```python
from x_twitter_scraper.types import APIKeyCreateResponse, APIKeyListResponse, APIKeyRevokeResponse
```

Methods:

- <code title="post /api-keys">client.api_keys.<a href="./src/x_twitter_scraper/resources/api_keys.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/api_key_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /api-keys">client.api_keys.<a href="./src/x_twitter_scraper/resources/api_keys.py">list</a>() -> <a href="./src/x_twitter_scraper/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /api-keys/{id}">client.api_keys.<a href="./src/x_twitter_scraper/resources/api_keys.py">revoke</a>(id) -> <a href="./src/x_twitter_scraper/types/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>

# Subscribe

Types:

```python
from x_twitter_scraper.types import SubscribeCreateResponse
```

Methods:

- <code title="post /subscribe">client.subscribe.<a href="./src/x_twitter_scraper/resources/subscribe.py">create</a>() -> <a href="./src/x_twitter_scraper/types/subscribe_create_response.py">SubscribeCreateResponse</a></code>

# Compose

Types:

```python
from x_twitter_scraper.types import ComposeCreateResponse
```

Methods:

- <code title="post /compose">client.compose.<a href="./src/x_twitter_scraper/resources/compose.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/compose_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/compose_create_response.py">ComposeCreateResponse</a></code>

# Drafts

Types:

```python
from x_twitter_scraper.types import DraftCreateResponse, DraftRetrieveResponse, DraftListResponse
```

Methods:

- <code title="post /drafts">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/draft_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draft_create_response.py">DraftCreateResponse</a></code>
- <code title="get /drafts/{id}">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/draft_retrieve_response.py">DraftRetrieveResponse</a></code>
- <code title="get /drafts">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/draft_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draft_list_response.py">DraftListResponse</a></code>
- <code title="delete /drafts/{id}">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">delete</a>(id) -> None</code>

# Styles

Types:

```python
from x_twitter_scraper.types import (
    StyleRetrieveResponse,
    StyleUpdateResponse,
    StyleListResponse,
    StyleAnalyzeResponse,
    StyleCompareResponse,
    StyleGetPerformanceResponse,
)
```

Methods:

- <code title="get /styles/{username}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">retrieve</a>(username) -> <a href="./src/x_twitter_scraper/types/style_retrieve_response.py">StyleRetrieveResponse</a></code>
- <code title="put /styles/{username}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">update</a>(username, \*\*<a href="src/x_twitter_scraper/types/style_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_update_response.py">StyleUpdateResponse</a></code>
- <code title="get /styles">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">list</a>() -> <a href="./src/x_twitter_scraper/types/style_list_response.py">StyleListResponse</a></code>
- <code title="delete /styles/{username}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">delete</a>(username) -> None</code>
- <code title="post /styles">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">analyze</a>(\*\*<a href="src/x_twitter_scraper/types/style_analyze_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_analyze_response.py">StyleAnalyzeResponse</a></code>
- <code title="get /styles/compare">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">compare</a>(\*\*<a href="src/x_twitter_scraper/types/style_compare_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_compare_response.py">StyleCompareResponse</a></code>
- <code title="get /styles/{username}/performance">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">get_performance</a>(username) -> <a href="./src/x_twitter_scraper/types/style_get_performance_response.py">StyleGetPerformanceResponse</a></code>

# Radar

Types:

```python
from x_twitter_scraper.types import RadarRetrieveTrendingTopicsResponse
```

Methods:

- <code title="get /radar">client.radar.<a href="./src/x_twitter_scraper/resources/radar.py">retrieve_trending_topics</a>(\*\*<a href="src/x_twitter_scraper/types/radar_retrieve_trending_topics_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/radar_retrieve_trending_topics_response.py">RadarRetrieveTrendingTopicsResponse</a></code>

# Monitors

Types:

```python
from x_twitter_scraper.types import (
    MonitorCreateResponse,
    MonitorRetrieveResponse,
    MonitorUpdateResponse,
    MonitorListResponse,
    MonitorDeactivateResponse,
)
```

Methods:

- <code title="post /monitors">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/monitor_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="get /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/monitor_retrieve_response.py">MonitorRetrieveResponse</a></code>
- <code title="patch /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/monitor_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="get /monitors">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors.py">list</a>() -> <a href="./src/x_twitter_scraper/types/monitor_list_response.py">MonitorListResponse</a></code>
- <code title="delete /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors.py">deactivate</a>(id) -> <a href="./src/x_twitter_scraper/types/monitor_deactivate_response.py">MonitorDeactivateResponse</a></code>

# Events

Types:

```python
from x_twitter_scraper.types import EventRetrieveResponse, EventListResponse
```

Methods:

- <code title="get /events/{id}">client.events.<a href="./src/x_twitter_scraper/resources/events.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/event_retrieve_response.py">EventRetrieveResponse</a></code>
- <code title="get /events">client.events.<a href="./src/x_twitter_scraper/resources/events.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/event_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/event_list_response.py">EventListResponse</a></code>

# Extractions

Types:

```python
from x_twitter_scraper.types import (
    ExtractionRetrieveResponse,
    ExtractionListResponse,
    ExtractionEstimateCostResponse,
    ExtractionRunResponse,
)
```

Methods:

- <code title="get /extractions/{id}">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/extraction_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_retrieve_response.py">ExtractionRetrieveResponse</a></code>
- <code title="get /extractions">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_list_response.py">ExtractionListResponse</a></code>
- <code title="post /extractions/estimate">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">estimate_cost</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_estimate_cost_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_estimate_cost_response.py">ExtractionEstimateCostResponse</a></code>
- <code title="get /extractions/{id}/export">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">export_results</a>(id, \*\*<a href="src/x_twitter_scraper/types/extraction_export_results_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /extractions">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">run</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_run_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_run_response.py">ExtractionRunResponse</a></code>

# Draws

Types:

```python
from x_twitter_scraper.types import DrawRetrieveResponse, DrawListResponse, DrawRunResponse
```

Methods:

- <code title="get /draws/{id}">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/draw_retrieve_response.py">DrawRetrieveResponse</a></code>
- <code title="get /draws">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/draw_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draw_list_response.py">DrawListResponse</a></code>
- <code title="get /draws/{id}/export">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">export</a>(id, \*\*<a href="src/x_twitter_scraper/types/draw_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /draws">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">run</a>(\*\*<a href="src/x_twitter_scraper/types/draw_run_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draw_run_response.py">DrawRunResponse</a></code>

# Webhooks

Types:

```python
from x_twitter_scraper.types import (
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeactivateResponse,
    WebhookListDeliveriesResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/webhook_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="patch /webhooks/{id}">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/webhook_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">list</a>() -> <a href="./src/x_twitter_scraper/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">deactivate</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_deactivate_response.py">WebhookDeactivateResponse</a></code>
- <code title="get /webhooks/{id}/deliveries">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">list_deliveries</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_list_deliveries_response.py">WebhookListDeliveriesResponse</a></code>
- <code title="post /webhooks/{id}/test">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">test</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_test_response.py">WebhookTestResponse</a></code>

# Integrations

Types:

```python
from x_twitter_scraper.types import (
    IntegrationCreateResponse,
    IntegrationRetrieveResponse,
    IntegrationUpdateResponse,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationListDeliveriesResponse,
    IntegrationSendTestResponse,
)
```

Methods:

- <code title="post /integrations">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/integration_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/integration_create_response.py">IntegrationCreateResponse</a></code>
- <code title="get /integrations/{id}">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/integration_retrieve_response.py">IntegrationRetrieveResponse</a></code>
- <code title="patch /integrations/{id}">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/integration_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/integration_update_response.py">IntegrationUpdateResponse</a></code>
- <code title="get /integrations">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">list</a>() -> <a href="./src/x_twitter_scraper/types/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="delete /integrations/{id}">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">delete</a>(id) -> <a href="./src/x_twitter_scraper/types/integration_delete_response.py">IntegrationDeleteResponse</a></code>
- <code title="get /integrations/{id}/deliveries">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">list_deliveries</a>(id, \*\*<a href="src/x_twitter_scraper/types/integration_list_deliveries_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/integration_list_deliveries_response.py">IntegrationListDeliveriesResponse</a></code>
- <code title="post /integrations/{id}/test">client.integrations.<a href="./src/x_twitter_scraper/resources/integrations.py">send_test</a>(id) -> <a href="./src/x_twitter_scraper/types/integration_send_test_response.py">IntegrationSendTestResponse</a></code>

# X

Types:

```python
from x_twitter_scraper.types import (
    XGetArticleResponse,
    XGetHomeTimelineResponse,
    XGetNotificationsResponse,
)
```

Methods:

- <code title="get /x/articles/{tweetId}">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_article</a>(tweet_id) -> <a href="./src/x_twitter_scraper/types/x_get_article_response.py">XGetArticleResponse</a></code>
- <code title="get /x/timeline">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_home_timeline</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_home_timeline_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_home_timeline_response.py">XGetHomeTimelineResponse</a></code>
- <code title="get /x/notifications">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_notifications</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_notifications_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_notifications_response.py">XGetNotificationsResponse</a></code>
- <code title="get /x/trends">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_trends</a>() -> None</code>

## Tweets

Types:

```python
from x_twitter_scraper.types.x import (
    TweetCreateResponse,
    TweetRetrieveResponse,
    TweetDeleteResponse,
    TweetGetFavoritersResponse,
    TweetGetQuotesResponse,
    TweetGetRepliesResponse,
    TweetGetRetweetersResponse,
    TweetGetThreadResponse,
    TweetSearchResponse,
)
```

Methods:

- <code title="post /x/tweets">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_create_response.py">TweetCreateResponse</a></code>
- <code title="get /x/tweets/{tweetId}">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">retrieve</a>(tweet_id) -> <a href="./src/x_twitter_scraper/types/x/tweet_retrieve_response.py">TweetRetrieveResponse</a></code>
- <code title="get /x/tweets">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_list_params.py">params</a>) -> None</code>
- <code title="delete /x/tweets/{tweetId}">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">delete</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_delete_response.py">TweetDeleteResponse</a></code>
- <code title="get /x/tweets/{id}/favoriters">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_favoriters</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_favoriters_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_favoriters_response.py">TweetGetFavoritersResponse</a></code>
- <code title="get /x/tweets/{id}/quotes">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_quotes</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_quotes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_quotes_response.py">TweetGetQuotesResponse</a></code>
- <code title="get /x/tweets/{id}/replies">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_replies</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_replies_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_replies_response.py">TweetGetRepliesResponse</a></code>
- <code title="get /x/tweets/{id}/retweeters">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_retweeters</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_retweeters_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_retweeters_response.py">TweetGetRetweetersResponse</a></code>
- <code title="get /x/tweets/{id}/thread">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_thread</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_thread_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_thread_response.py">TweetGetThreadResponse</a></code>
- <code title="get /x/tweets/search">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">search</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_search_response.py">TweetSearchResponse</a></code>

### Like

Types:

```python
from x_twitter_scraper.types.x.tweets import LikeCreateResponse, LikeDeleteResponse
```

Methods:

- <code title="post /x/tweets/{tweetId}/like">client.x.tweets.like.<a href="./src/x_twitter_scraper/resources/x/tweets/like.py">create</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/like_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/like_create_response.py">LikeCreateResponse</a></code>
- <code title="delete /x/tweets/{tweetId}/like">client.x.tweets.like.<a href="./src/x_twitter_scraper/resources/x/tweets/like.py">delete</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/like_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/like_delete_response.py">LikeDeleteResponse</a></code>

### Retweet

Types:

```python
from x_twitter_scraper.types.x.tweets import RetweetCreateResponse, RetweetDeleteResponse
```

Methods:

- <code title="post /x/tweets/{tweetId}/retweet">client.x.tweets.retweet.<a href="./src/x_twitter_scraper/resources/x/tweets/retweet.py">create</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/retweet_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/retweet_create_response.py">RetweetCreateResponse</a></code>
- <code title="delete /x/tweets/{tweetId}/retweet">client.x.tweets.retweet.<a href="./src/x_twitter_scraper/resources/x/tweets/retweet.py">delete</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/retweet_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/retweet_delete_response.py">RetweetDeleteResponse</a></code>

## Users

Types:

```python
from x_twitter_scraper.types.x import (
    UserRetrieveResponse,
    UserRetrieveFollowersYouKnowResponse,
    UserRetrieveLikesResponse,
    UserRetrieveMediaResponse,
    UserRetrieveTweetsResponse,
)
```

Methods:

- <code title="get /x/users/{username}">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve</a>(username) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /x/users/batch">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_batch</a>(\*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_batch_params.py">params</a>) -> None</code>
- <code title="get /x/users/{id}/followers">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_followers_params.py">params</a>) -> None</code>
- <code title="get /x/users/{id}/followers-you-know">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_followers_you_know</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_followers_you_know_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_followers_you_know_response.py">UserRetrieveFollowersYouKnowResponse</a></code>
- <code title="get /x/users/{id}/following">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_following</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_following_params.py">params</a>) -> None</code>
- <code title="get /x/users/{id}/likes">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_likes</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_likes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_likes_response.py">UserRetrieveLikesResponse</a></code>
- <code title="get /x/users/{id}/media">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_media</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_media_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_media_response.py">UserRetrieveMediaResponse</a></code>
- <code title="get /x/users/{id}/mentions">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_mentions</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_mentions_params.py">params</a>) -> None</code>
- <code title="get /x/users/search">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_search</a>(\*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_search_params.py">params</a>) -> None</code>
- <code title="get /x/users/{id}/tweets">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_tweets</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_tweets_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_tweets_response.py">UserRetrieveTweetsResponse</a></code>
- <code title="get /x/users/{id}/verified-followers">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_verified_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_verified_followers_params.py">params</a>) -> None</code>

### Follow

Types:

```python
from x_twitter_scraper.types.x.users import FollowCreateResponse, FollowDeleteAllResponse
```

Methods:

- <code title="post /x/users/{userId}/follow">client.x.users.follow.<a href="./src/x_twitter_scraper/resources/x/users/follow.py">create</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/users/follow_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/users/follow_create_response.py">FollowCreateResponse</a></code>
- <code title="delete /x/users/{userId}/follow">client.x.users.follow.<a href="./src/x_twitter_scraper/resources/x/users/follow.py">delete_all</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/users/follow_delete_all_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/users/follow_delete_all_response.py">FollowDeleteAllResponse</a></code>

## Followers

Types:

```python
from x_twitter_scraper.types.x import FollowerRetrieveCheckResponse
```

Methods:

- <code title="get /x/followers/check">client.x.followers.<a href="./src/x_twitter_scraper/resources/x/followers.py">retrieve_check</a>(\*\*<a href="src/x_twitter_scraper/types/x/follower_retrieve_check_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/follower_retrieve_check_response.py">FollowerRetrieveCheckResponse</a></code>

## Dm

Types:

```python
from x_twitter_scraper.types.x import DmUpdateResponse, DmRetrieveHistoryResponse
```

Methods:

- <code title="post /x/dm/{userId}">client.x.dm.<a href="./src/x_twitter_scraper/resources/x/dm.py">update</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/dm_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/dm_update_response.py">DmUpdateResponse</a></code>
- <code title="get /x/dm/{userId}/history">client.x.dm.<a href="./src/x_twitter_scraper/resources/x/dm.py">retrieve_history</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/dm_retrieve_history_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/dm_retrieve_history_response.py">DmRetrieveHistoryResponse</a></code>

## Media

Types:

```python
from x_twitter_scraper.types.x import MediaCreateResponse, MediaDownloadResponse
```

Methods:

- <code title="post /x/media">client.x.media.<a href="./src/x_twitter_scraper/resources/x/media.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/media_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/media_create_response.py">MediaCreateResponse</a></code>
- <code title="post /x/media/download">client.x.media.<a href="./src/x_twitter_scraper/resources/x/media.py">download</a>(\*\*<a href="src/x_twitter_scraper/types/x/media_download_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/media_download_response.py">MediaDownloadResponse</a></code>

## Profile

Types:

```python
from x_twitter_scraper.types.x import (
    ProfilePatchAllResponse,
    ProfileUpdateAvatarResponse,
    ProfileUpdateBannerResponse,
)
```

Methods:

- <code title="patch /x/profile">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">patch_all</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_patch_all_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_patch_all_response.py">ProfilePatchAllResponse</a></code>
- <code title="patch /x/profile/avatar">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">update_avatar</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_update_avatar_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_update_avatar_response.py">ProfileUpdateAvatarResponse</a></code>
- <code title="patch /x/profile/banner">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">update_banner</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_update_banner_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_update_banner_response.py">ProfileUpdateBannerResponse</a></code>

## Communities

Types:

```python
from x_twitter_scraper.types.x import (
    CommunityCreateResponse,
    CommunityDeleteResponse,
    CommunityRetrieveInfoResponse,
)
```

Methods:

- <code title="post /x/communities">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_create_response.py">CommunityCreateResponse</a></code>
- <code title="delete /x/communities/{id}">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">delete</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_delete_response.py">CommunityDeleteResponse</a></code>
- <code title="get /x/communities/{id}/info">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_info</a>(id) -> <a href="./src/x_twitter_scraper/types/x/community_retrieve_info_response.py">CommunityRetrieveInfoResponse</a></code>
- <code title="get /x/communities/{id}/members">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_members</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_members_params.py">params</a>) -> None</code>
- <code title="get /x/communities/{id}/moderators">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_moderators</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_moderators_params.py">params</a>) -> None</code>
- <code title="get /x/communities/search">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_search</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_search_params.py">params</a>) -> None</code>

### Join

Types:

```python
from x_twitter_scraper.types.x.communities import JoinCreateResponse, JoinDeleteAllResponse
```

Methods:

- <code title="post /x/communities/{id}/join">client.x.communities.join.<a href="./src/x_twitter_scraper/resources/x/communities/join.py">create</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/join_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/communities/join_create_response.py">JoinCreateResponse</a></code>
- <code title="delete /x/communities/{id}/join">client.x.communities.join.<a href="./src/x_twitter_scraper/resources/x/communities/join.py">delete_all</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/join_delete_all_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/communities/join_delete_all_response.py">JoinDeleteAllResponse</a></code>

### Tweets

Methods:

- <code title="get /x/communities/tweets">client.x.communities.tweets.<a href="./src/x_twitter_scraper/resources/x/communities/tweets.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/communities/tweet_list_params.py">params</a>) -> None</code>

## Accounts

Types:

```python
from x_twitter_scraper.types.x import (
    AccountCreateResponse,
    AccountRetrieveResponse,
    AccountListResponse,
    AccountDeleteResponse,
    AccountReauthResponse,
)
```

Methods:

- <code title="post /x/accounts">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/account_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_create_response.py">AccountCreateResponse</a></code>
- <code title="get /x/accounts/{id}">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/x/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /x/accounts">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">list</a>() -> <a href="./src/x_twitter_scraper/types/x/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /x/accounts/{id}">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">delete</a>(id) -> <a href="./src/x_twitter_scraper/types/x/account_delete_response.py">AccountDeleteResponse</a></code>
- <code title="post /x/accounts/{id}/reauth">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">reauth</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/account_reauth_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_reauth_response.py">AccountReauthResponse</a></code>

## Bookmarks

Types:

```python
from x_twitter_scraper.types.x import BookmarkListResponse, BookmarkRetrieveFoldersResponse
```

Methods:

- <code title="get /x/bookmarks">client.x.bookmarks.<a href="./src/x_twitter_scraper/resources/x/bookmarks.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/bookmark_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/bookmark_list_response.py">BookmarkListResponse</a></code>
- <code title="get /x/bookmarks/folders">client.x.bookmarks.<a href="./src/x_twitter_scraper/resources/x/bookmarks.py">retrieve_folders</a>() -> <a href="./src/x_twitter_scraper/types/x/bookmark_retrieve_folders_response.py">BookmarkRetrieveFoldersResponse</a></code>

## Lists

Methods:

- <code title="get /x/lists/{id}/followers">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_followers_params.py">params</a>) -> None</code>
- <code title="get /x/lists/{id}/members">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_members</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_members_params.py">params</a>) -> None</code>
- <code title="get /x/lists/{id}/tweets">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_tweets</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_tweets_params.py">params</a>) -> None</code>

# Trends

Types:

```python
from x_twitter_scraper.types import TrendListResponse
```

Methods:

- <code title="get /trends">client.trends.<a href="./src/x_twitter_scraper/resources/trends.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/trend_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/trend_list_response.py">TrendListResponse</a></code>

# Bot

Types:

```python
from x_twitter_scraper.types import BotTrackUsageResponse
```

Methods:

- <code title="post /bot/usage">client.bot.<a href="./src/x_twitter_scraper/resources/bot/bot.py">track_usage</a>(\*\*<a href="src/x_twitter_scraper/types/bot_track_usage_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/bot_track_usage_response.py">BotTrackUsageResponse</a></code>

## PlatformLinks

Types:

```python
from x_twitter_scraper.types.bot import (
    PlatformLinkCreateResponse,
    PlatformLinkDeleteResponse,
    PlatformLinkLookupResponse,
)
```

Methods:

- <code title="post /bot/platform-links">client.bot.platform_links.<a href="./src/x_twitter_scraper/resources/bot/platform_links.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/bot/platform_link_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/bot/platform_link_create_response.py">PlatformLinkCreateResponse</a></code>
- <code title="delete /bot/platform-links">client.bot.platform_links.<a href="./src/x_twitter_scraper/resources/bot/platform_links.py">delete</a>(\*\*<a href="src/x_twitter_scraper/types/bot/platform_link_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/bot/platform_link_delete_response.py">PlatformLinkDeleteResponse</a></code>
- <code title="get /bot/platform-links/lookup">client.bot.platform_links.<a href="./src/x_twitter_scraper/resources/bot/platform_links.py">lookup</a>(\*\*<a href="src/x_twitter_scraper/types/bot/platform_link_lookup_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/bot/platform_link_lookup_response.py">PlatformLinkLookupResponse</a></code>

# Support

## Tickets

Types:

```python
from x_twitter_scraper.types.support import (
    TicketCreateResponse,
    TicketRetrieveResponse,
    TicketUpdateResponse,
    TicketListResponse,
    TicketReplyResponse,
)
```

Methods:

- <code title="post /support/tickets">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/support/ticket_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_create_response.py">TicketCreateResponse</a></code>
- <code title="get /support/tickets/{id}">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/support/ticket_retrieve_response.py">TicketRetrieveResponse</a></code>
- <code title="patch /support/tickets/{id}">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/support/ticket_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_update_response.py">TicketUpdateResponse</a></code>
- <code title="get /support/tickets">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">list</a>() -> <a href="./src/x_twitter_scraper/types/support/ticket_list_response.py">TicketListResponse</a></code>
- <code title="post /support/tickets/{id}/messages">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">reply</a>(id, \*\*<a href="src/x_twitter_scraper/types/support/ticket_reply_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_reply_response.py">TicketReplyResponse</a></code>

# Credits

Types:

```python
from x_twitter_scraper.types import CreditRetrieveBalanceResponse, CreditTopupBalanceResponse
```

Methods:

- <code title="get /credits">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">retrieve_balance</a>() -> <a href="./src/x_twitter_scraper/types/credit_retrieve_balance_response.py">CreditRetrieveBalanceResponse</a></code>
- <code title="post /credits/topup">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">topup_balance</a>(\*\*<a href="src/x_twitter_scraper/types/credit_topup_balance_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/credit_topup_balance_response.py">CreditTopupBalanceResponse</a></code>
