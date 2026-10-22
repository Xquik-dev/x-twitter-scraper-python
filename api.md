# Shared Types

```python
from x_twitter_scraper.types import (
    Community,
    CommunityAnalytics,
    CommunityAnalyticsMetric,
    CommunityPage,
    CommunityTopic,
    ContentDisclosure,
    EmbeddedTweet,
    Error,
    ErrorCode,
    EventType,
    PaginatedTweets,
    PaginatedUsers,
    SearchTweet,
    SoftIntervention,
    TweetMedia,
    UserProfile,
)
```

# Account

Types

```python
from x_twitter_scraper.types import (
    AccountRetrieveResponse,
    AccountSetXUsernameResponse,
    AccountUpdateLocaleResponse,
)
```

Methods

- <code title="get /account">client.account.<a href="./src/x_twitter_scraper/resources/account.py">retrieve</a>() -> <a href="./src/x_twitter_scraper/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="put /account/x-identity">client.account.<a href="./src/x_twitter_scraper/resources/account.py">set_x_username</a>(\*\*<a href="src/x_twitter_scraper/types/account_set_x_username_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/account_set_x_username_response.py">AccountSetXUsernameResponse</a></code>
- <code title="patch /account">client.account.<a href="./src/x_twitter_scraper/resources/account.py">update_locale</a>(\*\*<a href="src/x_twitter_scraper/types/account_update_locale_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/account_update_locale_response.py">AccountUpdateLocaleResponse</a></code>

# Subscribe

Types

```python
from x_twitter_scraper.types import SubscribeCreateResponse
```

Methods

- <code title="post /subscribe">client.subscribe.<a href="./src/x_twitter_scraper/resources/subscribe.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/subscribe_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/subscribe_create_response.py">SubscribeCreateResponse</a></code>

# Compose

Types

```python
from x_twitter_scraper.types import ComposeCreateResponse
```

Methods

- <code title="post /compose">client.compose.<a href="./src/x_twitter_scraper/resources/compose.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/compose_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/compose_create_response.py">ComposeCreateResponse</a></code>

# Drafts

Types

```python
from x_twitter_scraper.types import Draft, DraftDetail, DraftCreateResponse, DraftListResponse
```

Methods

- <code title="post /drafts">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/draft_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draft_create_response.py">DraftCreateResponse</a></code>
- <code title="get /drafts/{id}">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/draft_detail.py">DraftDetail</a></code>
- <code title="get /drafts">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/draft_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draft_list_response.py">DraftListResponse</a></code>
- <code title="delete /drafts/{id}">client.drafts.<a href="./src/x_twitter_scraper/resources/drafts.py">delete</a>(id) -> None</code>

# Styles

Types

```python
from x_twitter_scraper.types import (
    StyleProfile,
    StyleProfileSummary,
    StyleListResponse,
    StyleCompareResponse,
    StyleGetPerformanceResponse,
)
```

Methods

- <code title="get /styles/{id}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/style_profile.py">StyleProfile</a></code>
- <code title="put /styles/{id}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/style_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_profile.py">StyleProfile</a></code>
- <code title="get /styles">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/style_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_list_response.py">StyleListResponse</a></code>
- <code title="delete /styles/{id}">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">delete</a>(id) -> None</code>
- <code title="post /styles">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">analyze</a>(\*\*<a href="src/x_twitter_scraper/types/style_analyze_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_profile.py">StyleProfile</a></code>
- <code title="get /styles/compare">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">compare</a>(\*\*<a href="src/x_twitter_scraper/types/style_compare_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/style_compare_response.py">StyleCompareResponse</a></code>
- <code title="get /styles/{id}/performance">client.styles.<a href="./src/x_twitter_scraper/resources/styles.py">get_performance</a>(id) -> <a href="./src/x_twitter_scraper/types/style_get_performance_response.py">StyleGetPerformanceResponse</a></code>

# Radar

Types

```python
from x_twitter_scraper.types import RadarItem, RadarRetrieveTrendingTopicsResponse
```

Methods

- <code title="get /radar">client.radar.<a href="./src/x_twitter_scraper/resources/radar.py">retrieve_trending_topics</a>(\*\*<a href="src/x_twitter_scraper/types/radar_retrieve_trending_topics_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/radar_retrieve_trending_topics_response.py">RadarRetrieveTrendingTopicsResponse</a></code>

# Monitors

Types

```python
from x_twitter_scraper.types import (
    Monitor,
    MonitorCreateResponse,
    MonitorListResponse,
    MonitorDeactivateResponse,
)
```

Methods

- <code title="post /monitors">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors/monitors.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/monitor_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="get /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors/monitors.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/monitor.py">Monitor</a></code>
- <code title="patch /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors/monitors.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/monitor_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitor.py">Monitor</a></code>
- <code title="get /monitors">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors/monitors.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/monitor_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitor_list_response.py">MonitorListResponse</a></code>
- <code title="delete /monitors/{id}">client.monitors.<a href="./src/x_twitter_scraper/resources/monitors/monitors.py">deactivate</a>(id) -> <a href="./src/x_twitter_scraper/types/monitor_deactivate_response.py">MonitorDeactivateResponse</a></code>

## Keywords

Types

```python
from x_twitter_scraper.types.monitors import (
    KeywordCreateResponse,
    KeywordRetrieveResponse,
    KeywordUpdateResponse,
    KeywordListResponse,
    KeywordDeactivateResponse,
)
```

Methods

- <code title="post /monitors/keywords">client.monitors.keywords.<a href="./src/x_twitter_scraper/resources/monitors/keywords.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/monitors/keyword_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitors/keyword_create_response.py">KeywordCreateResponse</a></code>
- <code title="get /monitors/keywords/{id}">client.monitors.keywords.<a href="./src/x_twitter_scraper/resources/monitors/keywords.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/monitors/keyword_retrieve_response.py">KeywordRetrieveResponse</a></code>
- <code title="patch /monitors/keywords/{id}">client.monitors.keywords.<a href="./src/x_twitter_scraper/resources/monitors/keywords.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/monitors/keyword_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitors/keyword_update_response.py">KeywordUpdateResponse</a></code>
- <code title="get /monitors/keywords">client.monitors.keywords.<a href="./src/x_twitter_scraper/resources/monitors/keywords.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/monitors/keyword_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/monitors/keyword_list_response.py">KeywordListResponse</a></code>
- <code title="delete /monitors/keywords/{id}">client.monitors.keywords.<a href="./src/x_twitter_scraper/resources/monitors/keywords.py">deactivate</a>(id) -> <a href="./src/x_twitter_scraper/types/monitors/keyword_deactivate_response.py">KeywordDeactivateResponse</a></code>

# Events

Types

```python
from x_twitter_scraper.types import Event, EventDetail, EventListResponse
```

Methods

- <code title="get /events/{id}">client.events.<a href="./src/x_twitter_scraper/resources/events.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/event_detail.py">EventDetail</a></code>
- <code title="get /events">client.events.<a href="./src/x_twitter_scraper/resources/events.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/event_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/event_list_response.py">EventListResponse</a></code>
- <code title="get /events/stream">client.events.<a href="./src/x_twitter_scraper/resources/events.py">stream</a>() -> Stream[<a href="./src/x_twitter_scraper/types/event.py">Event</a>]</code>

# Extractions

Types

```python
from x_twitter_scraper.types import (
    ExtractionJob,
    ExtractionRetrieveResponse,
    ExtractionListResponse,
    ExtractionCancelResponse,
    ExtractionEstimateCostResponse,
    ExtractionRunResponse,
)
```

Methods

- <code title="get /extractions/{id}">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/extraction_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_retrieve_response.py">ExtractionRetrieveResponse</a></code>
- <code title="get /extractions">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_list_response.py">ExtractionListResponse</a></code>
- <code title="delete /extractions/{id}">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">cancel</a>(id) -> <a href="./src/x_twitter_scraper/types/extraction_cancel_response.py">ExtractionCancelResponse</a></code>
- <code title="post /extractions/estimate">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">estimate_cost</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_estimate_cost_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_estimate_cost_response.py">ExtractionEstimateCostResponse</a></code>
- <code title="get /extractions/{id}/export">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">export_results</a>(id, \*\*<a href="src/x_twitter_scraper/types/extraction_export_results_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /extractions">client.extractions.<a href="./src/x_twitter_scraper/resources/extractions.py">run</a>(\*\*<a href="src/x_twitter_scraper/types/extraction_run_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/extraction_run_response.py">ExtractionRunResponse</a></code>

# Draws

Types

```python
from x_twitter_scraper.types import (
    DrawDetail,
    DrawListItem,
    Winner,
    DrawRetrieveResponse,
    DrawListResponse,
    DrawRunResponse,
)
```

Methods

- <code title="get /draws/{id}">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/draw_retrieve_response.py">DrawRetrieveResponse</a></code>
- <code title="get /draws">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/draw_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draw_list_response.py">DrawListResponse</a></code>
- <code title="get /draws/{id}/export">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">export</a>(id, \*\*<a href="src/x_twitter_scraper/types/draw_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /draws">client.draws.<a href="./src/x_twitter_scraper/resources/draws.py">run</a>(\*\*<a href="src/x_twitter_scraper/types/draw_run_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/draw_run_response.py">DrawRunResponse</a></code>

# Webhooks

Types

```python
from x_twitter_scraper.types import (
    Delivery,
    Webhook,
    WebhookCreateResponse,
    WebhookListResponse,
    WebhookCreateTelegramLinkResponse,
    WebhookDeactivateResponse,
    WebhookListDeliveriesResponse,
    WebhookResumeResponse,
    WebhookTestResponse,
)
```

Methods

- <code title="post /webhooks">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/webhook_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="patch /webhooks/{id}">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/webhook_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/webhook_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="post /webhooks/telegram">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">create_telegram_link</a>(\*\*<a href="src/x_twitter_scraper/types/webhook_create_telegram_link_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_create_telegram_link_response.py">WebhookCreateTelegramLinkResponse</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">deactivate</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_deactivate_response.py">WebhookDeactivateResponse</a></code>
- <code title="get /webhooks/{id}/deliveries">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">list_deliveries</a>(id, \*\*<a href="src/x_twitter_scraper/types/webhook_list_deliveries_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/webhook_list_deliveries_response.py">WebhookListDeliveriesResponse</a></code>
- <code title="post /webhooks/{id}/resume">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">resume</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_resume_response.py">WebhookResumeResponse</a></code>
- <code title="post /webhooks/{id}/test">client.webhooks.<a href="./src/x_twitter_scraper/resources/webhooks.py">test</a>(id) -> <a href="./src/x_twitter_scraper/types/webhook_test_response.py">WebhookTestResponse</a></code>

# X

Types

```python
from x_twitter_scraper.types import (
    XAutocompleteSearchResponse,
    XGetArticleResponse,
    XGetHashflagsResponse,
    XGetNewsStoryVersionsResponse,
    XGetNotificationsResponse,
    XGetTrendLocationsResponse,
    XGetTrendsResponse,
    XGetTrendsHistoryResponse,
    XSearchPlacesResponse,
)
```

Methods

- <code title="get /x/search/autocomplete">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">autocomplete_search</a>(\*\*<a href="src/x_twitter_scraper/types/x_autocomplete_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_autocomplete_search_response.py">XAutocompleteSearchResponse</a></code>
- <code title="get /x/articles/{tweetId}">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_article</a>(tweet_id, \*\*<a href="src/x_twitter_scraper/types/x_get_article_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_article_response.py">XGetArticleResponse</a></code>
- <code title="get /x/hashflags">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_hashflags</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_hashflags_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_hashflags_response.py">XGetHashflagsResponse</a></code>
- <code title="get /x/timeline">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_home_timeline</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_home_timeline_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/news/{id}/versions">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_news_story_versions</a>(id, \*\*<a href="src/x_twitter_scraper/types/x_get_news_story_versions_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_news_story_versions_response.py">XGetNewsStoryVersionsResponse</a></code>
- <code title="get /x/notifications">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_notifications</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_notifications_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_notifications_response.py">XGetNotificationsResponse</a></code>
- <code title="get /x/trends/locations">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_trend_locations</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_trend_locations_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_trend_locations_response.py">XGetTrendLocationsResponse</a></code>
- <code title="get /x/trends">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_trends</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_trends_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_trends_response.py">XGetTrendsResponse</a></code>
- <code title="get /x/trends/history">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">get_trends_history</a>(\*\*<a href="src/x_twitter_scraper/types/x_get_trends_history_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_get_trends_history_response.py">XGetTrendsHistoryResponse</a></code>
- <code title="get /x/places/search">client.x.<a href="./src/x_twitter_scraper/resources/x/x.py">search_places</a>(\*\*<a href="src/x_twitter_scraper/types/x_search_places_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x_search_places_response.py">XSearchPlacesResponse</a></code>

## WriteActions

Types

```python
from x_twitter_scraper.types.x import WriteActionRetrieveResponse
```

Methods

- <code title="get /x/write-actions/{id}">client.x.write_actions.<a href="./src/x_twitter_scraper/resources/x/write_actions.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/x/write_action_retrieve_response.py">WriteActionRetrieveResponse</a></code>

## Analysis

Types

```python
from x_twitter_scraper.types.x import (
    AnalysisBrandResponse,
    AnalysisClassifyResponse,
    AnalysisMarketSignalsResponse,
    AnalysisNewsResponse,
    AnalysisSentimentResponse,
    AnalysisViralScoreResponse,
)
```

Methods

- <code title="post /x/analysis/brand">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">brand</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_brand_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_brand_response.py">AnalysisBrandResponse</a></code>
- <code title="post /x/analysis/classify">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">classify</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_classify_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_classify_response.py">AnalysisClassifyResponse</a></code>
- <code title="post /x/analysis/market-signals">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">market_signals</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_market_signals_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_market_signals_response.py">AnalysisMarketSignalsResponse</a></code>
- <code title="post /x/analysis/news">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">news</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_news_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_news_response.py">AnalysisNewsResponse</a></code>
- <code title="post /x/analysis/sentiment">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">sentiment</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_sentiment_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_sentiment_response.py">AnalysisSentimentResponse</a></code>
- <code title="post /x/analysis/viral-score">client.x.analysis.<a href="./src/x_twitter_scraper/resources/x/analysis.py">viral_score</a>(\*\*<a href="src/x_twitter_scraper/types/x/analysis_viral_score_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/analysis_viral_score_response.py">AnalysisViralScoreResponse</a></code>

## Tweets

Types

```python
from x_twitter_scraper.types.x import (
    TweetAuthor,
    TweetDetail,
    TweetCreateResponse,
    TweetRetrieveResponse,
    TweetListResponse,
    TweetDeleteResponse,
    TweetCheckRepostResponse,
    TweetEmbedResponse,
    TweetGetInsightsResponse,
    TweetGetRepliesResponse,
    TweetGetRetweeterIdsResponse,
    TweetGetSubtitlesResponse,
    TweetResolveLinksResponse,
    TweetSearchResponse,
    TweetTranslateResponse,
)
```

Methods

- <code title="post /x/tweets">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_create_response.py">TweetCreateResponse</a></code>
- <code title="get /x/tweets/{id}">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_retrieve_response.py">TweetRetrieveResponse</a></code>
- <code title="get /x/tweets">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_list_response.py">TweetListResponse</a></code>
- <code title="delete /x/tweets/{id}">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">delete</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_delete_response.py">TweetDeleteResponse</a></code>
- <code title="get /x/tweets/{id}/retweeters/check">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">check_repost</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_check_repost_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_check_repost_response.py">TweetCheckRepostResponse</a></code>
- <code title="get /x/tweets/{id}/embed">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">embed</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_embed_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_embed_response.py">TweetEmbedResponse</a></code>
- <code title="get /x/tweets/{id}/favoriters">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_favoriters</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_favoriters_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/tweets/{id}/hidden-replies">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_hidden_replies</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_hidden_replies_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/tweets/{id}/insights">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_insights</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_insights_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_insights_response.py">TweetGetInsightsResponse</a></code>
- <code title="get /x/tweets/{id}/quotes">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_quotes</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_quotes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/tweets/{id}/replies">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_replies</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_replies_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_replies_response.py">TweetGetRepliesResponse</a></code>
- <code title="get /x/tweets/{id}/retweeter-ids">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_retweeter_ids</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_retweeter_ids_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_retweeter_ids_response.py">TweetGetRetweeterIdsResponse</a></code>
- <code title="get /x/tweets/{id}/retweeters">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_retweeters</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_retweeters_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/tweets/{id}/subtitles">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_subtitles</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_subtitles_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_get_subtitles_response.py">TweetGetSubtitlesResponse</a></code>
- <code title="get /x/tweets/{id}/thread">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">get_thread</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_get_thread_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/tweets/top">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">list_top</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_list_top_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/links/resolve">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">resolve_links</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_resolve_links_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_resolve_links_response.py">TweetResolveLinksResponse</a></code>
- <code title="get /x/tweets/search">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">search</a>(\*\*<a href="src/x_twitter_scraper/types/x/tweet_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_search_response.py">TweetSearchResponse</a></code>
- <code title="get /x/tweets/{id}/translation">client.x.tweets.<a href="./src/x_twitter_scraper/resources/x/tweets/tweets.py">translate</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweet_translate_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweet_translate_response.py">TweetTranslateResponse</a></code>

### Like

Types

```python
from x_twitter_scraper.types.x.tweets import LikeCreateResponse, LikeDeleteResponse
```

Methods

- <code title="post /x/tweets/{id}/like">client.x.tweets.like.<a href="./src/x_twitter_scraper/resources/x/tweets/like.py">create</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/like_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/like_create_response.py">LikeCreateResponse</a></code>
- <code title="delete /x/tweets/{id}/like">client.x.tweets.like.<a href="./src/x_twitter_scraper/resources/x/tweets/like.py">delete</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/like_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/like_delete_response.py">LikeDeleteResponse</a></code>

### Retweet

Types

```python
from x_twitter_scraper.types.x.tweets import RetweetCreateResponse, RetweetDeleteResponse
```

Methods

- <code title="post /x/tweets/{id}/retweet">client.x.tweets.retweet.<a href="./src/x_twitter_scraper/resources/x/tweets/retweet.py">create</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/retweet_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/retweet_create_response.py">RetweetCreateResponse</a></code>
- <code title="delete /x/tweets/{id}/retweet">client.x.tweets.retweet.<a href="./src/x_twitter_scraper/resources/x/tweets/retweet.py">delete</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/tweets/retweet_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/tweets/retweet_delete_response.py">RetweetDeleteResponse</a></code>

## Users

Types

```python
from x_twitter_scraper.types.x import (
    UserRemoveFollowerResponse,
    UserRetrieveBatchResponse,
    UserRetrieveBatchTweetsResponse,
    UserRetrieveFollowerIdsResponse,
    UserRetrieveFollowersResponse,
    UserRetrieveFollowingResponse,
    UserRetrieveFollowingIdsResponse,
    UserRetrieveInsightsResponse,
    UserRetrieveListMembershipsResponse,
    UserRetrieveListsResponse,
    UserRetrieveLiveResponse,
    UserRetrieveVerifiedFollowersResponse,
    UserTranslateBioResponse,
)
```

Methods

- <code title="get /x/users/{id}">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/user_profile.py">UserProfile</a></code>
- <code title="post /x/users/{id}/remove-follower">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">remove_follower</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_remove_follower_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_remove_follower_response.py">UserRemoveFollowerResponse</a></code>
- <code title="get /x/users/{id}/affiliates">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_affiliates</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_affiliates_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/users/{id}/articles">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_articles</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_articles_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/batch">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_batch</a>(\*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_batch_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_batch_response.py">UserRetrieveBatchResponse</a></code>
- <code title="get /x/users/batch/tweets">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_batch_tweets</a>(\*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_batch_tweets_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_batch_tweets_response.py">UserRetrieveBatchTweetsResponse</a></code>
- <code title="get /x/users/{id}/follower-ids">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_follower_ids</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_follower_ids_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_follower_ids_response.py">UserRetrieveFollowerIdsResponse</a></code>
- <code title="get /x/users/{id}/followers">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_followers_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_followers_response.py">UserRetrieveFollowersResponse</a></code>
- <code title="get /x/users/{id}/followers-you-know">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_followers_you_know</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_followers_you_know_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/users/{id}/following">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_following</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_following_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_following_response.py">UserRetrieveFollowingResponse</a></code>
- <code title="get /x/users/{id}/following-ids">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_following_ids</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_following_ids_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_following_ids_response.py">UserRetrieveFollowingIdsResponse</a></code>
- <code title="get /x/users/{id}/highlights">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_highlights</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_highlights_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/{id}/insights">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_insights</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_insights_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_insights_response.py">UserRetrieveInsightsResponse</a></code>
- <code title="get /x/users/{id}/likes">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_likes</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_likes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/{id}/list-memberships">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_list_memberships</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_list_memberships_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_list_memberships_response.py">UserRetrieveListMembershipsResponse</a></code>
- <code title="get /x/users/{id}/lists">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_lists</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_lists_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_lists_response.py">UserRetrieveListsResponse</a></code>
- <code title="get /x/users/{id}/live">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_live</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_live_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_live_response.py">UserRetrieveLiveResponse</a></code>
- <code title="get /x/users/{id}/media">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_media</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_media_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/{id}/mentions">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_mentions</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_mentions_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/{id}/replies">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_replies</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_replies_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/search">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_search</a>(\*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/users/{id}/similar">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_similar</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_similar_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/users/{id}/subscriptions">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_subscriptions</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_subscriptions_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/users/{id}/tweets">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_tweets</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_tweets_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/users/{id}/verified-followers">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">retrieve_verified_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_retrieve_verified_followers_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_retrieve_verified_followers_response.py">UserRetrieveVerifiedFollowersResponse</a></code>
- <code title="get /x/users/{id}/translation">client.x.users.<a href="./src/x_twitter_scraper/resources/x/users/users.py">translate_bio</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/user_translate_bio_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/user_translate_bio_response.py">UserTranslateBioResponse</a></code>

### Follow

Types

```python
from x_twitter_scraper.types.x.users import FollowCreateResponse, FollowDeleteAllResponse
```

Methods

- <code title="post /x/users/{id}/follow">client.x.users.follow.<a href="./src/x_twitter_scraper/resources/x/users/follow.py">create</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/users/follow_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/users/follow_create_response.py">FollowCreateResponse</a></code>
- <code title="delete /x/users/{id}/follow">client.x.users.follow.<a href="./src/x_twitter_scraper/resources/x/users/follow.py">delete_all</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/users/follow_delete_all_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/users/follow_delete_all_response.py">FollowDeleteAllResponse</a></code>

## Followers

Types

```python
from x_twitter_scraper.types.x import FollowerCheckResponse
```

Methods

- <code title="get /x/followers/check">client.x.followers.<a href="./src/x_twitter_scraper/resources/x/followers.py">check</a>(\*\*<a href="src/x_twitter_scraper/types/x/follower_check_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/follower_check_response.py">FollowerCheckResponse</a></code>

## Jobs

Types

```python
from x_twitter_scraper.types.x import JobRetrieveResponse, JobListLocationsResponse, JobSearchResponse
```

Methods

- <code title="get /x/jobs/{id}">client.x.jobs.<a href="./src/x_twitter_scraper/resources/x/jobs.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/job_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /x/jobs/locations">client.x.jobs.<a href="./src/x_twitter_scraper/resources/x/jobs.py">list_locations</a>(\*\*<a href="src/x_twitter_scraper/types/x/job_list_locations_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/job_list_locations_response.py">JobListLocationsResponse</a></code>
- <code title="get /x/jobs/search">client.x.jobs.<a href="./src/x_twitter_scraper/resources/x/jobs.py">search</a>(\*\*<a href="src/x_twitter_scraper/types/x/job_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/job_search_response.py">JobSearchResponse</a></code>

## Dm

Types

```python
from x_twitter_scraper.types.x import DmDeleteMessageResponse, DmRetrieveHistoryResponse, DmSendResponse
```

Methods

- <code title="delete /x/dm/{userId}/messages/{messageId}">client.x.dm.<a href="./src/x_twitter_scraper/resources/x/dm.py">delete_message</a>(message_id, \*, user_id, \*\*<a href="src/x_twitter_scraper/types/x/dm_delete_message_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/dm_delete_message_response.py">DmDeleteMessageResponse</a></code>
- <code title="get /x/dm/{userId}/history">client.x.dm.<a href="./src/x_twitter_scraper/resources/x/dm.py">retrieve_history</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/dm_retrieve_history_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/dm_retrieve_history_response.py">DmRetrieveHistoryResponse</a></code>
- <code title="post /x/dm/{userId}">client.x.dm.<a href="./src/x_twitter_scraper/resources/x/dm.py">send</a>(user_id, \*\*<a href="src/x_twitter_scraper/types/x/dm_send_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/dm_send_response.py">DmSendResponse</a></code>

## Media

Types

```python
from x_twitter_scraper.types.x import MediaDownloadResponse, MediaUploadResponse
```

Methods

- <code title="post /x/media/download">client.x.media.<a href="./src/x_twitter_scraper/resources/x/media.py">download</a>(\*\*<a href="src/x_twitter_scraper/types/x/media_download_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/media_download_response.py">MediaDownloadResponse</a></code>
- <code title="post /x/media">client.x.media.<a href="./src/x_twitter_scraper/resources/x/media.py">upload</a>(\*\*<a href="src/x_twitter_scraper/types/x/media_upload_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/media_upload_response.py">MediaUploadResponse</a></code>

## Profile

Types

```python
from x_twitter_scraper.types.x import (
    ProfileUpdateResponse,
    ProfileUpdateAvatarResponse,
    ProfileUpdateBannerResponse,
)
```

Methods

- <code title="patch /x/profile">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">update</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="patch /x/profile/avatar">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">update_avatar</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_update_avatar_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_update_avatar_response.py">ProfileUpdateAvatarResponse</a></code>
- <code title="patch /x/profile/banner">client.x.profile.<a href="./src/x_twitter_scraper/resources/x/profile.py">update_banner</a>(\*\*<a href="src/x_twitter_scraper/types/x/profile_update_banner_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/profile_update_banner_response.py">ProfileUpdateBannerResponse</a></code>

## Communities

Types

```python
from x_twitter_scraper.types.x import (
    CommunityCreateResponse,
    CommunityDeleteResponse,
    CommunityListSuggestedResponse,
    CommunityListTopicsResponse,
    CommunityRetrieveInfoResponse,
)
```

Methods

- <code title="post /x/communities">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_create_response.py">CommunityCreateResponse</a></code>
- <code title="delete /x/communities/{id}">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">delete</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_delete_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_delete_response.py">CommunityDeleteResponse</a></code>
- <code title="get /x/communities/find">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">find</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_find_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/community_page.py">CommunityPage</a></code>
- <code title="get /x/communities/popular">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">list_popular</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_list_popular_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/community_page.py">CommunityPage</a></code>
- <code title="get /x/communities/suggested">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">list_suggested</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_list_suggested_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_list_suggested_response.py">CommunityListSuggestedResponse</a></code>
- <code title="get /x/communities/topics">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">list_topics</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_list_topics_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_list_topics_response.py">CommunityListTopicsResponse</a></code>
- <code title="get /x/communities/{id}/analytics">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_analytics</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_analytics_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/community_analytics.py">CommunityAnalytics</a></code>
- <code title="get /x/communities/{id}/info">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_info</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_info_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_retrieve_info_response.py">CommunityRetrieveInfoResponse</a></code>
- <code title="get /x/communities/{id}/members">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_members</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_members_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/communities/{id}/moderators">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_moderators</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_moderators_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>
- <code title="get /x/communities/search">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">retrieve_search</a>(\*\*<a href="src/x_twitter_scraper/types/x/community_retrieve_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/communities/{id}/members/search">client.x.communities.<a href="./src/x_twitter_scraper/resources/x/communities/communities.py">search_members</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/community_search_members_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_users.py">PaginatedUsers</a></code>

### Join

Types

```python
from x_twitter_scraper.types.x.communities import JoinCreateResponse, JoinDeleteAllResponse
```

Methods

- <code title="post /x/communities/{id}/join">client.x.communities.join.<a href="./src/x_twitter_scraper/resources/x/communities/join.py">create</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/join_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/communities/join_create_response.py">JoinCreateResponse</a></code>
- <code title="delete /x/communities/{id}/join">client.x.communities.join.<a href="./src/x_twitter_scraper/resources/x/communities/join.py">delete_all</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/join_delete_all_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/communities/join_delete_all_response.py">JoinDeleteAllResponse</a></code>

### Tweets

Methods

- <code title="get /x/communities/tweets">client.x.communities.tweets.<a href="./src/x_twitter_scraper/resources/x/communities/tweets.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/communities/tweet_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/communities/{id}/tweets">client.x.communities.tweets.<a href="./src/x_twitter_scraper/resources/x/communities/tweets.py">list_by_community</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/tweet_list_by_community_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>

### Media

Methods

- <code title="get /x/communities/{id}/media">client.x.communities.media.<a href="./src/x_twitter_scraper/resources/x/communities/media.py">list</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/communities/media_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>

## Accounts

Types

```python
from x_twitter_scraper.types.x import (
    XAccount,
    XAccountDetail,
    AccountCreateResponse,
    AccountListResponse,
    AccountDeleteResponse,
    AccountBulkRetryResponse,
    AccountReauthResponse,
)
```

Methods

- <code title="post /x/accounts">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/x/account_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_create_response.py">AccountCreateResponse</a></code>
- <code title="get /x/accounts/{id}">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/x/x_account_detail.py">XAccountDetail</a></code>
- <code title="get /x/accounts">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/account_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /x/accounts/{id}">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">delete</a>(id) -> <a href="./src/x_twitter_scraper/types/x/account_delete_response.py">AccountDeleteResponse</a></code>
- <code title="post /x/accounts/bulk-retry">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">bulk_retry</a>() -> <a href="./src/x_twitter_scraper/types/x/account_bulk_retry_response.py">AccountBulkRetryResponse</a></code>
- <code title="post /x/accounts/{id}/reauth">client.x.accounts.<a href="./src/x_twitter_scraper/resources/x/accounts.py">reauth</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/account_reauth_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_reauth_response.py">AccountReauthResponse</a></code>

## AccountConnectionChallenges

Types

```python
from x_twitter_scraper.types.x import AccountConnectionChallengeSubmitResponse
```

Methods

- <code title="post /x/account-connection-challenges/{id}/submit">client.x.account_connection_challenges.<a href="./src/x_twitter_scraper/resources/x/account_connection_challenges.py">submit</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/account_connection_challenge_submit_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/account_connection_challenge_submit_response.py">AccountConnectionChallengeSubmitResponse</a></code>

## AccountConnectionAttempts

Types

```python
from x_twitter_scraper.types.x import AccountConnectionAttemptRetrieveResponse
```

Methods

- <code title="get /x/account-connection-attempts/{id}">client.x.account_connection_attempts.<a href="./src/x_twitter_scraper/resources/x/account_connection_attempts.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/x/account_connection_attempt_retrieve_response.py">AccountConnectionAttemptRetrieveResponse</a></code>

## Bookmarks

Types

```python
from x_twitter_scraper.types.x import BookmarkRetrieveFoldersResponse
```

Methods

- <code title="get /x/bookmarks">client.x.bookmarks.<a href="./src/x_twitter_scraper/resources/x/bookmarks.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/x/bookmark_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>
- <code title="get /x/bookmarks/folders">client.x.bookmarks.<a href="./src/x_twitter_scraper/resources/x/bookmarks.py">retrieve_folders</a>(\*\*<a href="src/x_twitter_scraper/types/x/bookmark_retrieve_folders_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/bookmark_retrieve_folders_response.py">BookmarkRetrieveFoldersResponse</a></code>

## Lists

Types

```python
from x_twitter_scraper.types.x import (
    ListRetrieveResponse,
    ListRetrieveFollowersResponse,
    ListRetrieveMembersResponse,
    ListRetrieveSearchResponse,
)
```

Methods

- <code title="get /x/lists/{id}">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/list_retrieve_response.py">ListRetrieveResponse</a></code>
- <code title="get /x/lists/{id}/followers">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_followers</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_followers_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/list_retrieve_followers_response.py">ListRetrieveFollowersResponse</a></code>
- <code title="get /x/lists/{id}/members">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_members</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_members_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/list_retrieve_members_response.py">ListRetrieveMembersResponse</a></code>
- <code title="get /x/lists/search">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_search</a>(\*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/list_retrieve_search_response.py">ListRetrieveSearchResponse</a></code>
- <code title="get /x/lists/{id}/tweets">client.x.lists.<a href="./src/x_twitter_scraper/resources/x/lists.py">retrieve_tweets</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/list_retrieve_tweets_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/shared/paginated_tweets.py">PaginatedTweets</a></code>

## Broadcasts

Types

```python
from x_twitter_scraper.types.x import BroadcastRetrieveResponse
```

Methods

- <code title="get /x/broadcasts/{id}">client.x.broadcasts.<a href="./src/x_twitter_scraper/resources/x/broadcasts.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/broadcast_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/broadcast_retrieve_response.py">BroadcastRetrieveResponse</a></code>

## CommunityNotes

Types

```python
from x_twitter_scraper.types.x import (
    CommunityNoteListContributorDeletedNotesResponse,
    CommunityNoteListContributorNotesResponse,
    CommunityNoteRetrieveContributorResponse,
)
```

Methods

- <code title="get /x/community-notes/contributors/{alias}/deleted-notes">client.x.community_notes.<a href="./src/x_twitter_scraper/resources/x/community_notes.py">list_contributor_deleted_notes</a>(alias, \*\*<a href="src/x_twitter_scraper/types/x/community_note_list_contributor_deleted_notes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_note_list_contributor_deleted_notes_response.py">CommunityNoteListContributorDeletedNotesResponse</a></code>
- <code title="get /x/community-notes/contributors/{alias}/notes">client.x.community_notes.<a href="./src/x_twitter_scraper/resources/x/community_notes.py">list_contributor_notes</a>(alias, \*\*<a href="src/x_twitter_scraper/types/x/community_note_list_contributor_notes_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_note_list_contributor_notes_response.py">CommunityNoteListContributorNotesResponse</a></code>
- <code title="get /x/community-notes/contributors/{alias}">client.x.community_notes.<a href="./src/x_twitter_scraper/resources/x/community_notes.py">retrieve_contributor</a>(alias, \*\*<a href="src/x_twitter_scraper/types/x/community_note_retrieve_contributor_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/community_note_retrieve_contributor_response.py">CommunityNoteRetrieveContributorResponse</a></code>

## Spaces

Types

```python
from x_twitter_scraper.types.x import SpaceRetrieveResponse, SpaceRetrieveReplayResponse, SpaceSearchResponse
```

Methods

- <code title="get /x/spaces/{id}">client.x.spaces.<a href="./src/x_twitter_scraper/resources/x/spaces.py">retrieve</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/space_retrieve_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/space_retrieve_response.py">SpaceRetrieveResponse</a></code>
- <code title="get /x/spaces/{id}/replay">client.x.spaces.<a href="./src/x_twitter_scraper/resources/x/spaces.py">retrieve_replay</a>(id, \*\*<a href="src/x_twitter_scraper/types/x/space_retrieve_replay_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/space_retrieve_replay_response.py">SpaceRetrieveReplayResponse</a></code>
- <code title="get /x/spaces/search">client.x.spaces.<a href="./src/x_twitter_scraper/resources/x/spaces.py">search</a>(\*\*<a href="src/x_twitter_scraper/types/x/space_search_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/x/space_search_response.py">SpaceSearchResponse</a></code>

# Trends

Types

```python
from x_twitter_scraper.types import TrendListResponse
```

Methods

- <code title="get /trends">client.trends.<a href="./src/x_twitter_scraper/resources/trends.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/trend_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/trend_list_response.py">TrendListResponse</a></code>

# Support

## Attachments

Methods

- <code title="get /support/attachments/{id}">client.support.attachments.<a href="./src/x_twitter_scraper/resources/support/attachments.py">download</a>(id) -> BinaryAPIResponse</code>

## Tickets

Types

```python
from x_twitter_scraper.types.support import (
    TicketCreateResponse,
    TicketRetrieveResponse,
    TicketUpdateResponse,
    TicketListResponse,
    TicketReplyResponse,
)
```

Methods

- <code title="post /support/tickets">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/support/ticket_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_create_response.py">TicketCreateResponse</a></code>
- <code title="get /support/tickets/{id}">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">retrieve</a>(id) -> <a href="./src/x_twitter_scraper/types/support/ticket_retrieve_response.py">TicketRetrieveResponse</a></code>
- <code title="patch /support/tickets/{id}">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">update</a>(id, \*\*<a href="src/x_twitter_scraper/types/support/ticket_update_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_update_response.py">TicketUpdateResponse</a></code>
- <code title="get /support/tickets">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">list</a>(\*\*<a href="src/x_twitter_scraper/types/support/ticket_list_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_list_response.py">TicketListResponse</a></code>
- <code title="post /support/tickets/{id}/messages">client.support.tickets.<a href="./src/x_twitter_scraper/resources/support/tickets.py">reply</a>(id, \*\*<a href="src/x_twitter_scraper/types/support/ticket_reply_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/support/ticket_reply_response.py">TicketReplyResponse</a></code>

# Credits

Types

```python
from x_twitter_scraper.types import (
    CreditRetrieveBalanceResponse,
    CreditRetrieveTopupStatusResponse,
    CreditTopupBalanceResponse,
)
```

Methods

- <code title="get /credits/topup/redirect">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">redirect_topup_checkout</a>(\*\*<a href="src/x_twitter_scraper/types/credit_redirect_topup_checkout_params.py">params</a>) -> None</code>
- <code title="get /credits">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">retrieve_balance</a>() -> <a href="./src/x_twitter_scraper/types/credit_retrieve_balance_response.py">CreditRetrieveBalanceResponse</a></code>
- <code title="get /credits/topup/status">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">retrieve_topup_status</a>(\*\*<a href="src/x_twitter_scraper/types/credit_retrieve_topup_status_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/credit_retrieve_topup_status_response.py">CreditRetrieveTopupStatusResponse</a></code>
- <code title="post /credits/topup">client.credits.<a href="./src/x_twitter_scraper/resources/credits.py">topup_balance</a>(\*\*<a href="src/x_twitter_scraper/types/credit_topup_balance_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/credit_topup_balance_response.py">CreditTopupBalanceResponse</a></code>

# GuestWallets

Types

```python
from x_twitter_scraper.types import (
    GuestWalletAmount,
    GuestWalletCreateResponse,
    GuestWalletRetrieveStatusResponse,
    GuestWalletTopupResponse,
)
```

Methods

- <code title="post /guest-wallets">client.guest_wallets.<a href="./src/x_twitter_scraper/resources/guest_wallets.py">create</a>(\*\*<a href="src/x_twitter_scraper/types/guest_wallet_create_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/guest_wallet_create_response.py">GuestWalletCreateResponse</a></code>
- <code title="get /guest-wallets/status">client.guest_wallets.<a href="./src/x_twitter_scraper/resources/guest_wallets.py">retrieve_status</a>() -> <a href="./src/x_twitter_scraper/types/guest_wallet_retrieve_status_response.py">GuestWalletRetrieveStatusResponse</a></code>
- <code title="post /guest-wallets/topups">client.guest_wallets.<a href="./src/x_twitter_scraper/resources/guest_wallets.py">topup</a>(\*\*<a href="src/x_twitter_scraper/types/guest_wallet_topup_params.py">params</a>) -> <a href="./src/x_twitter_scraper/types/guest_wallet_topup_response.py">GuestWalletTopupResponse</a></code>
