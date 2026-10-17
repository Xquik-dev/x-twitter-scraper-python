# Changelog

## Unreleased

- Embedded parent, quoted and retweeted posts carry every tweet field and the author.
- User profiles and tweet users return optional `override_verified_year` in `identity_verification`, the year X shows as the start of verification in place of `verified_since_msec`.
- The check scripts remove their temp dirs on every exit, including a failed step and a signal.

## 0.16.0 (2026-10-16)

This release adds the response fields, event types and file uploads the SDK dropped. A field check against the API spec found them.

### New fields and values

- User profiles return `profile_picture_original` and `redirects_to_username`. Space participants, broadcasters, job accounts, article authors, Community member previews and search suggestions return `profile_picture_original`.
- The links and accounts in tombstone and interstitial notices return `screen_name` and `text`.
- `EventType` adds `follower.added`, `follower.removed`, `profile.followers.changed` and `profile.following.changed`. Account monitors, webhooks and events take and return them. Keyword monitors take the 10 post types only.
- Event data gains the `DataMonitorFollow` variant, with `followed_at`, `followed_at_exact` and `reason`. Follow event data that carries none of them reads as `DataMonitorLegacyPost` with the same fields, so branch on `event.type` to find follow events. Profile change data gains `change`, and its `previous` and `current` take counts.
- Account monitors return `insufficient_credits` as a `paused_reason`. Keyword monitors return `paused_at` and `paused_reason`.
- `account.update_locale`, `drafts.create` and `webhooks.create` return `ignored_fields`. `drafts.create` returns `DraftCreateResponse`, a `DraftDetail` subclass.
- Follower, following, verified follower and List reads return `UserListPage`, a `PaginatedUsers` subclass with `scan_limit`.
- `x.tweets.get_replies` returns `partial_before`.
- Compose results read the new multiplier note "Source default. Production value can vary." and the old one.

### File uploads

- `x.media.upload`, `x.profile.update_avatar` and `x.profile.update_banner` take `file` as well as `url`. `x.media.upload` also takes `is_long_video`. A file sends a multipart request.
- `support.tickets.create` and `support.tickets.reply` take `attachments`, 1 to 4 files.
- `content` is optional when you send `attachments`. A ticket or reply can carry files and no text.
- The README upload sample passes the required `idempotency_key`.

### Compatibility

- `XAccount` and `XAccountDetail` drop a timestamp field the API stopped returning. It always read None. Other code written for 0.15.0 keeps working, and no method, type or parameter is removed.
- `url` and `content` are optional keyword arguments now, because `file` or `attachments` can replace them. A call with neither raises `TypeError`.
- With Pydantic 1, follow events still parse as `DataMonitorLegacyPost` with their fields as extras, and `previous` and `current` of a count event read as strings. Pydantic 1 takes the first union member that fits, so `DataMonitorFollow` sits last.

## 0.15.0 (2026-10-15)

2 existing methods gain the parameter, fields and query types the API spec added.

### Changes

- `x.get_trends` takes `at`, a past time or a span such as `24h`, and reads what was trending on Twitter then. The response gains `captured_at`, when Xquik read the list from X, and `requested_at`, the time `at` asked for.
- `x.spaces.search` accepts `Live` and `Upcoming` as `query_type`. They list Spaces on air now and scheduled ones, as X's Spaces search does.

### Compatibility

- Code written for 0.14.0 keeps working. Both changes only add.

## 0.14.0 (2026-10-15)

This release adds 5 methods from the current API spec.
The SDK now covers 180 of the 186 spec operations. The other 6 search the Xquik docs or need a dashboard sign-in, so the SDK leaves them out.

### New methods

- `x.get_trends_history` reads the trends X showed for a place over a range of time. It takes `from_` for the API's `from` parameter, because `from` is a Python keyword.
- `x.get_news_story_versions` reads each version X wrote of a news story, oldest first.
- `x.community_notes` is a new resource with `retrieve_contributor`, `list_contributor_notes` and `list_contributor_deleted_notes`. They read a Community Notes contributor's note and rating counts, the notes they wrote with their posts, and the notes they deleted.

### Compatibility

- Code written for 0.13 keeps working. No existing method, type or parameter changed.

## 0.13.1 (2026-10-14)

The API and its behavior are the same as in 0.13.0.

### Documentation

- The README uses sentence case headings, active voice and whole sentences. Its facts, links and legal lines stay the same.
- The README samples have no comments. The text around each sample says what it shows.

## 0.13.0 (2026-10-13)

This release adds 50 methods from the current API spec.
It is the first release on PyPI after 0.11.2, because 0.12.0 was never uploaded there. It includes the 0.12.0 changes.

### New methods

- `events.stream` reads monitor events as server-sent events.
- `webhooks.create_telegram_link` returns a link that connects a Telegram chat.
- `x` gains `autocomplete_search`, `get_hashflags`, `get_trend_locations` and `search_places`.
- `x.analysis` gains `brand`, `classify`, `market_signals`, `news`, `sentiment` and `viral_score`, which analyze posts with AI.
- `x.broadcasts.retrieve` reads a live broadcast.
- `x.communities` gains `find`, `list_popular`, `list_suggested`, `list_topics` and `search_members`.
- `x.communities.media.list` reads media posted in a Community.
- `x.dm.delete_message` deletes 1 DM from the account's side.
- `x.jobs` gains `list_locations`, `retrieve` and `search`, which read X job listings.
- `x.lists.retrieve` reads a List, and `x.lists.retrieve_search` finds Lists.
- `x.spaces` gains `retrieve`, `retrieve_replay` and `search`, which read Spaces.
- `x.tweets` gains `check_repost`, `embed`, `get_hidden_replies`, `get_insights`, `get_retweeter_ids`, `get_subtitles`, `list_top`, `resolve_links` and `translate`.
- `x.users` gains `retrieve_affiliates`, `retrieve_articles`, `retrieve_batch_tweets`, `retrieve_follower_ids`, `retrieve_following_ids`, `retrieve_highlights`, `retrieve_insights`, `retrieve_list_memberships`, `retrieve_lists`, `retrieve_live`, `retrieve_similar`, `retrieve_subscriptions` and `translate_bio`.

### Changes

- 72 existing methods match the current spec. New optional parameters include `fields`, `omit`, `cursor` and `limit`.
- Monitors, keyword monitors and draws accept the current fields, such as `name` and `idempotency_key`.
- Doc comments use the current prices. An active monitor costs 30 credits per hour, or 720 per day.
- `x.tweets.list` returns `TweetListResponse`, a `PaginatedTweets` subclass that adds `skipped`.
- 10 response fields that held plain dictionaries are typed models now. They are `Event.data`, `EventDetail.data`, the `job` and the `results` rows of `extractions.retrieve`, and the `entities` of tweets, their long-form notes and their quoted tweets.
- Code written for 0.11.2 keeps working. Parameters and fields that the spec no longer lists stay available, and the next section covers the 2 deprecations.
- The new shared models are `Community`, `CommunityPage` and `CommunityTopic`.

### Upgrading from 0.11 & 0.12

Code written for 0.11.2 runs on 0.13 without changes.
2 older ways of calling the SDK now emit a `DeprecationWarning` and go away in a later minor version.

The first is dict access on the values that were dictionaries in 0.11 & 0.12 and are models in 0.13.

- `Event.data` and `EventDetail.data`
- `extractions.retrieve(...).job` and each row of `extractions.retrieve(...).results`
- `entities` on a tweet, on its long-form note and on its quoted tweet

On these models `value["key"]`, `value.get("key")`, `"key" in value`, `value.keys()`, `value.values()` and `value.items()` still work with the JSON key names.
They return the JSON values, so a timestamp stays a string such as `2026-09-11T20:24:45.000Z`.
Keys come in the model's field order, which can differ from the order in the response.
Iteration, `len()` and `dict(value)` need `to_dict()`.
Switch to attribute access or `to_dict()`.

```python
# 0.11 & 0.12
event.data["likeCount"]
row.get("xUsername")
tweet.entities["urls"][0]["expanded_url"]

# 0.13
event.data.like_count
row.x_username
tweet.entities.urls[0].expanded_url
row.to_dict()["xUsername"]
```

The second is the `min_faves` keyword, which `min_likes` replaces.
`min_faves` still works on the 9 tweet and user methods that took it in 0.11, and it sends the same filter as `min_likes`.
When a call passes both, `min_likes` wins.

```python
# 0.11
client.x.tweets.search(q="xquik", min_faves=25)

# 0.13
client.x.tweets.search(q="xquik", min_likes=25)
```

## 0.12.0 (2026-09-12)

- Add optional retweet timestamps with nullable `retweeted_at` response fields.
- Align extraction, profile, and tweet contracts with the current API.
- Preserve eager iterable serialization across synchronous and asynchronous requests.

## 0.11.2 (2026-08-21)

Full Changelog: [v0.11.1...v0.11.2](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.11.1...v0.11.2)

### Documentation

* remove repeated Python SDK copy and clarify examples

## 0.11.1 (2026-08-20)

Full Changelog: [v0.11.0...v0.11.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.11.0...v0.11.1)

### Chores

* refresh all Python dependencies ([#47](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/47)) ([ab7ac3a](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/ab7ac3a14ba35f379f35241d5558a111ca2de52b))


### Documentation

* refine public Python SDK text ([811c7c2](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/811c7c28c26b25967283942c7a2b35ea112dee5a))

## 0.11.0 (2026-08-12)

Full Changelog: [v0.10.1...v0.11.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.10.1...v0.11.0)

### Features

* **api:** sync public contracts ([184f599](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/184f599c3f27391cdeb1f3657abb79f42509c809))

## 0.10.1 (2026-08-11)

Full Changelog: [v0.10.0...v0.10.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.10.0...v0.10.1)

### Features

* **api:** api update ([1fead25](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/1fead25d1da63f3f26dd08e75aba089ac487ace4))

## 0.10.0 (2026-08-11)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([0382bcc](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/0382bcc811e1705b67dd83e49249447c5684ae76))

## 0.9.0 (2026-08-11)

Full Changelog: [v0.8.1...v0.9.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.8.1...v0.9.0)

### Features

* **api:** api update ([6001ecb](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/6001ecbc6504d11d83fbebe0a3cffd83713e71bd))

## 0.8.1 (2026-08-11)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.8.0...v0.8.1)

### Chores

* **deps:** bump github/codeql-action/upload-sarif from 4.37.1 to 4.37.6 ([#35](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/35)) ([d5909c0](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/d5909c0c19439d56c82de4257c3935304a0fb534))
* **deps:** bump ossf/scorecard-action from 2.4.3 to 2.4.4 ([#37](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/37)) ([e985625](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/e985625b02fe0aa011cbd718de6f6f0665926804))
* **deps:** bump pypa/gh-action-pypi-publish from 1.14.1 to 1.14.2 ([#42](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/42)) ([0f33a5e](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/0f33a5e9488c363e47942f4e35aeebd72c979f46))

## 0.8.0 (2026-07-31)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** add complete reply extraction, rich response contracts, and typed account outcomes ([23ab238](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/23ab238d37c98eaa10ed10867d7a5e4d855f9294))

## 0.7.0 (2026-07-29)

Full Changelog: [v0.6.1...v0.7.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.6.1...v0.7.0)

### Features

* **api:** api update ([b63b37b](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/b63b37b882b4d227a542f0404604927912b60e99))
* **api:** api update ([533e09c](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/533e09c3b13682cc872ad9bac273dbc9f3de00ac))

## 0.6.1 (2026-07-28)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.6.0...v0.6.1)

### Chores

* **deps:** bump google/clusterfuzzlite/actions/build_fuzzers ([#26](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/26)) ([579f53a](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/579f53a63f327d7f38167ebfc1e1771e7ed77f2f))
* **deps:** bump google/clusterfuzzlite/actions/run_fuzzers ([#25](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/25)) ([846c5ff](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/846c5ffd557a950265176758310b1a57d1e77871))
* **deps:** bump pypa/gh-action-pypi-publish from 1.14.0 to 1.14.1 ([#27](https://github.com/Xquik-dev/x-twitter-scraper-python/issues/27)) ([f8d425d](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/f8d425d49a4813c7e1a427a302fc1f22a479300d))

## 0.6.0 (2026-07-24)

Full Changelog: [v0.5.2...v0.6.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.5.2...v0.6.0)

### Features

* add OpenSSF Gold quality gates ([ea3f5ef](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/ea3f5efbb4ca806f9910aa5eaf37298d258b9636))


### Bug Fixes

* audit locked Python dependencies ([b3427e6](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/b3427e6ea683a2cc983ad6ef4fc3c69ed3922063))


### Chores

* add per-file license evidence ([9c46658](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/9c466581fd61a8314fadfb5330bad5fe53ad4b90))


### Documentation

* clarify repository discovery ([32c6e61](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/32c6e61978018053b8077111c37c23bc711ceac1))

## 0.5.2 (2026-07-23)

Full Changelog: [v0.5.1...v0.5.2](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.5.1...v0.5.2)

### Documentation

* map common X data tasks ([9c5827e](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/9c5827e8a0ec1fbdffe66938bfaddff357fe7f01))

## 0.5.1 (2026-07-22)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.5.0...v0.5.1)

### Chores

* sync generated SDK contracts ([5873bd3](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/5873bd3a62b3f1fa9ff76e9f729527e8a9f0f57f))

## 0.5.0 (2026-07-22)

Full Changelog: [v0.4.3...v0.5.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.4.3...v0.5.0)

### Features

* **api:** propagate durable write actions ([71d3e5f](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/71d3e5f072f8f3d15bf65e1b2f2ab2d5404479dd))
* **api:** propagate production write-action contract ([8d10d43](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/8d10d435084eae9d61d8ddc72efe9a76f5cdc133))

## 0.4.2 (2026-07-14)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.4.1...v0.4.2)

### Security

* replace long-lived PyPI credentials with trusted publishing
* isolate builds from OIDC publishing and protect release tags
* update audited dependencies and require supported Python 3.10 or higher

## 0.4.1 (2026-04-25)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.4.0...v0.4.1)

### Chores

* **internal:** more robust bootstrap script ([69aa90c](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/69aa90c4cb22f105848e073fc4130e5c79db12aa))


### Documentation

* add Contributor Covenant 2.1 Code of Conduct ([06635a2](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/06635a2a9951934ecca52515211dbcec2714e46f))

## 0.4.0 (2026-04-22)

Full Changelog: [v0.3.1...v0.4.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.3.1...v0.4.0)

### Features

* **api:** api update ([ea97c97](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/ea97c97b83f9388dfe339655bd7e1e2f39bf8537))
* **api:** api update ([9ab5907](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/9ab59079a7538deaedc38cb221ba6421ff4dd39a))
* **api:** api update ([e6edd37](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/e6edd371ab5a80748ae26a0173206e89634c5da5))
* **api:** api update ([8e576ed](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/8e576ed647806a054a3f6b7f3be7dbcaffb36aef))


### Bug Fixes

* ensure file data are only sent as 1 parameter ([c86dcf1](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/c86dcf186aed37ef154028b708bc9cdf3a56bf39))
* escape ampersand in OpenAPI summaries for C# XML docs ([d2d9141](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/d2d9141e286e7f032f9aec934e93f33414c7221e))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([eb0688d](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/eb0688d0ae9da72c17a1b3550e0221d2f81a9ef4))


### Chores

* sync OpenAPI spec ([e7bfdb7](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/e7bfdb76972a4d2c6b5ddb5f0f1f815579fd175d))
* wire production_repo for all targets ([18d4cc3](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/18d4cc3d3c5796aaa637f3841224dfaa9e076a5b))

## 0.3.1 (2026-04-08)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.3.0...v0.3.1)

### Chores

* update SDK settings ([e2ff786](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/e2ff78681cdf29128336f66240aa1ca30ec605d3))

## 0.3.0 (2026-04-08)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([95f41f1](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/95f41f169819933331d1f5099dd49bec9f54c153))
* **api:** api update ([1099626](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/10996263a67c92aed9a32c6b08d665a314481efd))
* **api:** api update ([4da9b26](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/4da9b26da35aaf2d98decc7589df0a441decc54e))
* **api:** api update ([a4aab27](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/a4aab2774ebcd526a8d8e1bb141f245fa39a44da))
* **api:** api update ([6595833](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/65958335df38ea35208109db2248093a51f6563b))
* **api:** api update ([9059aff](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/9059aff529800e915fda0f8c3f1c0e19234f3057))
* **api:** api update ([e52e7fb](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/e52e7fba2cb13cdc2dd75fcfe4d281e7e28d445c))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([6ce9027](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/6ce902711cfc8cfac19f9adbddcc37762d0a6517))


### Chores

* update SDK settings ([60a1489](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/60a1489a526d1b98b2a11e39b835bd7ce552feb1))

## 0.2.0 (2026-04-01)

Full Changelog: [v0.1.3...v0.2.0](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.1.3...v0.2.0)

### Features

* **api:** api update ([dcfbf4f](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/dcfbf4f110165019fa851654c1911715009be8bb))
* **api:** api update ([017a1e4](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/017a1e4dd340690e38449cb036f40d3f6b1360b9))


### Chores

* update SDK settings ([3f45efe](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/3f45efe97044b419663bd45d9f769bf2af860c0b))

## 0.1.3 (2026-03-30)

Full Changelog: [v0.1.2...v0.1.3](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.1.2...v0.1.3)

### Chores

* update SDK settings ([a9763c8](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/a9763c8307b60d60168f39f087ab7c6451da3205))
* update SDK settings ([bf5ef3f](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/bf5ef3f999e34f9f0091e9314b053bc0081b9fa3))

## 0.1.2 (2026-03-30)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/Xquik-dev/x-twitter-scraper-python/compare/v0.1.1...v0.1.2)

### Chores

* resolve merge conflict, accept codegen changes ([ee87c63](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/ee87c630b5ab9e343dbf5f76a1ed3654339e7080))
* update SDK settings ([8ff770f](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/8ff770f05d0a8d2c21785d5c0a39d6c1cb70fd40))
* update SDK settings ([80207f7](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/80207f74d3d1e3dd8900bf4ad029231f603d1b3a))

## 0.1.1 (2026-03-30)

### Chores

* update SDK settings ([3ff9848](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/3ff98489454de0a9bcd2378c214e5407a7c04f53))

## 0.1.0 (2026-03-30)

### Features

* **api:** api update ([3e4e51b](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/3e4e51bfa74558e9d38d3b1aba5ff55785f638d3))
* **api:** api update ([f345fe8](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/f345fe83851e7bc2432ffb56c1e566e545a79161))
* **api:** api update ([9030f48](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/9030f48f5e1d4871688fe853ab5816e2c8bf568c))


### Chores

* update SDK settings ([a785253](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/a785253547f3d806ece2f24a3f9c5221f1002d07))
* update SDK settings ([8211ff8](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/8211ff844687e6cde33ffaeff033beccbd5004b6))
* update SDK settings ([eb39475](https://github.com/Xquik-dev/x-twitter-scraper-python/commit/eb39475765007dc0a20767d4811f542b3cda4b38))
