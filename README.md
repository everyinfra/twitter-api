# X (Twitter) API

[English](#english) · [中文](#中文)

## English

This repo reads public X (Twitter) data with Python or curl. You can search posts by keyword, read a single post and its replies, and look up an account's profile and posts. You need one EveryInfra API key. You do not need an X (Twitter) account or cookie. The same API also works as an MCP tool in Claude and Cursor. Billing is per call: these 5 capabilities cost $0.56 to $0.79 per 1,000 calls. Failed calls and empty results are not charged. The EveryInfra X (Twitter) API has 21 capabilities; 20 are available now. All are listed on the platform page: <https://everyinfra.com/en/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### Quick start

```bash
git clone https://github.com/everyinfra/twitter-api.git
cd twitter-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<your API key>
python main.py search "camping gear" --out posts.csv
python main.py post <post_id> --out post.json
python main.py replies <post_id> --out replies.csv
python main.py user <username>
python main.py posts <username> --out user_posts.csv
```

- For `post` and `replies`, pass the `id` from a `search` result. It is the number after x.com/<username>/status/. Do not pass the full link.
- For `user` and `posts`, pass the `author_username` from a `search` result.
- Without `--out`, the command prints the first 3 rows as JSON. With `--out`, it saves a .csv or .json file. The CSV has a BOM, so Excel opens it without garbled text.
- Register at everyinfra.com, then create the API key in the console. Steps: <https://everyinfra.com/en/docs?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api#quickstart>

### curl

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"twitter","action":"search","params":{"keyword":"camping gear"}}'
```

All capabilities use the same URL. Change `action` and `params` to call another one. Examples for `post`, `comments`, `profile`, and `user_posts` are in [examples/curl.sh](examples/curl.sh).

### Claude and Cursor (MCP)

The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. EveryInfra runs the server, so you install no local program.

Claude Code:

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor and other clients that read `mcp.json` ([examples/mcp.json](examples/mcp.json)):

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Custom connectors in Claude on the web and desktop, and ChatGPT, accept only a URL. Enter <https://api.everyinfra.com/mcp/all>, sign in to EveryInfra when asked, and allow access. You do not need to enter a key. Full steps: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### Price

| `action` | Per 1,000 calls |
|---|---|
| `search` | $0.79 |
| `post` | $0.56 |
| `comments` | $0.56 |
| `profile` | $0.56 |
| `user_posts` | $0.56 |

- Billing is per call, about $0.00056 to $0.00079 each. Failed calls, empty results, parameter errors, and authentication failures are not charged.
- A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- Prices for the other 15 available X (Twitter) capabilities are on the platform page: <https://everyinfra.com/en/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### Fields

The fields of each capability are documented on the English pages linked below.

- `search`: <https://everyinfra.com/en/twitter-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- `post`: <https://everyinfra.com/en/twitter-api/post?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- `comments`: <https://everyinfra.com/en/twitter-api/comments?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- `profile`: <https://everyinfra.com/en/twitter-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- `user_posts`: <https://everyinfra.com/en/twitter-api/user_posts?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### FAQ

**Do I need an X (Twitter) account or cookie to call the API?**

No. Send the `Authorization: Bearer` header with your API key. The request body holds `platform`, `action`, and the capability parameters. You do not scan a QR code, keep a login session, or open a browser.

**How much does it cost? Are failed calls charged? Is there a free allowance?**

Billing is per call, from $0.56 per 1,000 calls. Failed calls, empty results, parameter errors, and authentication failures are not charged. A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

**Can I connect the X (Twitter) API to Claude or Cursor?**

Yes. The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. You install no local program. Setup for Claude, Cursor, ChatGPT, and Claude Code: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>. An agent can then search X (Twitter) content, read comments, and look up accounts by itself.

**What legal points apply when I use X (Twitter) data?**

The EveryInfra Terms of Service require you to make sure your use of the data follows applicable law and the terms of the relevant platform. Do not use the data for anything illegal or anything that violates privacy or intellectual property rights. Do not use bulk scraping for harassment, fraud, or other abuse. When you use personal information such as nicknames and avatars, keep only the fields your business needs.

**Which X (Twitter) data can I get?**

The EveryInfra X (Twitter) API has 21 capabilities; 20 are available now:

- keyword search
- profile or object details
- user content
- post details
- comments
- trending list
- follower list
- following list
- media posts
- replies tab
- reposters
- Profiles by user ID
- about this account
- follow check
- community details
- community search
- user search
- video transcript
- thread
- community posts

Parameters and return fields for each capability are on the platform page: <https://everyinfra.com/en/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### Tested

Before release, we ran the 5 commands in Quick start against the live API with this repo's code.

| Command | Time (Singapore, UTC+8) | Rows | Charged |
|---|---|---|---|
| `python main.py search "camping gear" --out posts.csv` | 2026-11-21 09:26 | 25 | $0.000792 |
| `python main.py post <post_id> --out post.json` | 2026-11-21 09:26 | 1 | $0.000556 |
| `python main.py replies <post_id> --out replies.csv` | 2026-11-21 09:26 | 14 | $0.000556 |
| `python main.py user <username>` | 2026-11-21 09:27 | 1 | $0.000556 |
| `python main.py posts <username> --out user_posts.csv` | 2026-11-21 09:27 | 20 | $0.000556 |

## 中文

本仓库用 Python 或 curl 读 X (Twitter) 公开数据：按关键词搜帖子，读单条帖子和回复，查账号资料和他发布的帖子。只需一把 EveryInfra API Key，不用 X (Twitter) 账号和 Cookie，也能作为 MCP 工具接进 Claude、Cursor。按调用次数计费，这 5 个能力每千次 $0.56 到 $0.79，失败和空结果不收费。X (Twitter) 共 21 个能力，其中 20 个现在可用：<https://everyinfra.com/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### 快速开始

```bash
git clone https://github.com/everyinfra/twitter-api.git
cd twitter-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<你的 API Key>
python main.py search "camping gear" --out posts.csv
python main.py post <post_id> --out post.json
python main.py replies <post_id> --out replies.csv
python main.py user <username>
python main.py posts <username> --out user_posts.csv
```

- `post` 和 `replies` 传 `search` 结果里的 `id`，就是 x.com/用户名/status/ 后面那串数字，不要传完整链接。
- `user` 和 `posts` 传 `search` 结果里的 `author_username`。
- 不加 `--out` 时打印前 3 条 JSON；加 `--out` 存成 .csv 或 .json。CSV 带 BOM，Excel 直接打开不乱码。
- API Key 在 everyinfra.com 注册后到控制台创建，步骤见 <https://everyinfra.com/docs?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api#quickstart>

### 用 curl 调

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"twitter","action":"search","params":{"keyword":"camping gear"}}'
```

所有能力都发到同一个地址，换 `action` 和 `params` 就行；`post`、`comments`、`profile`、`user_posts` 的写法见 [examples/curl.sh](examples/curl.sh)。

### 接进 Claude、Cursor（MCP）

远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key；服务器由 EveryInfra 运行，不用装本地程序。

Claude Code：

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor 等读 `mcp.json` 的客户端（[examples/mcp.json](examples/mcp.json)）：

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Claude 网页版和桌面版的自定义连接器、ChatGPT 只能填网址：填 <https://api.everyinfra.com/mcp/all>，连接时登录 EveryInfra 并允许，不用填 Key。完整步骤见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### 价格

| 能力 | `action` | 每千次 |
|---|---|---|
| 关键词搜索 | `search` | $0.79 |
| 单条内容 | `post` | $0.56 |
| 评论 | `comments` | $0.56 |
| 主页或对象详情 | `profile` | $0.56 |
| 用户内容 | `user_posts` | $0.56 |

- 按调用次数计费，每次约 $0.00056 到 $0.00079；失败、空结果、参数错误和鉴权失败都不收费。
- 新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>
- X (Twitter) 其他 15 个可用能力的单价见平台页 <https://everyinfra.com/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### 返回字段

下面是这 5 个能力实测返回的字段，含义取自接口文档每条说明的第一句，完整说明在每张表下面的链接里。

#### `search`（关键词搜索）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `retweet_count` | 转发数。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `view_count` | 浏览/播放数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者在原平台的主页链接。 |
| `author_follower_count` | 作者粉丝数。 |
| `bookmark_count` | 书签（收藏）数。 |
| `language` | 内容语言代码（如 zh、en），由平台判定，可能不准。 |
| `conversation_id` | 所属对话串 ID（根推文 ID），同一串的回复据此归在一起。 |
| `is_quote` | 是否引用推文。 |
| `media` | 推文图片 / 视频：type（photo / video / animated_gif）、url（图片或视频封面）、width、height、duration_sec（视频秒数）、video_url（码率最高的 mp4）。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_avatar_url` | 作者头像图片链接（多数平台带签名、会过期）。 |
| `author_post_count` | 作者推文总数。 |
| `author_banner_url` | 作者主页横幅图链接。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

实测还返回了 `quote_count`、`is_reply`、`is_repost`、`author_bio`、`author_is_verified`、`author_following_count`、`author_created_at`、`reply_to_id`，接口文档里还没有它们的中文说明，表里没列。

完整参数和字段：<https://everyinfra.com/twitter-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

#### `post`（单条内容）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `retweet_count` | 转发数。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `view_count` | 浏览/播放数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者在原平台的主页链接。 |
| `author_follower_count` | 作者粉丝数。 |
| `bookmark_count` | 书签（收藏）数。 |
| `language` | 内容语言代码（如 zh、en），由平台判定，可能不准。 |
| `conversation_id` | 所属对话串 ID（根推文 ID），同一串的回复据此归在一起。 |
| `media` | 推文图片 / 视频：type（photo / video / animated_gif）、url（图片或视频封面）、width、height、duration_sec（视频秒数）、video_url（码率最高的 mp4）。 |
| `hashtags` | 正文里的话题标签数组，按出现顺序；没有时不出现这个字段。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_avatar_url` | 作者头像图片链接（多数平台带签名、会过期）。 |
| `author_post_count` | 作者推文总数。 |
| `author_media_count` | 作者发过的媒体数。 |
| `author_banner_url` | 作者主页横幅图链接。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

实测还返回了 `quote_count`、`is_reply`、`is_pinned`、`author_bio`、`author_is_verified`、`author_following_count`、`author_created_at`，接口文档里还没有它们的中文说明，表里没列。

完整参数和字段：<https://everyinfra.com/twitter-api/post?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

#### `comments`（评论）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `retweet_count` | 转发数。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `view_count` | 浏览/播放数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者在原平台的主页链接。 |
| `author_follower_count` | 作者粉丝数。 |
| `bookmark_count` | 书签（收藏）数。 |
| `language` | 内容语言代码（如 zh、en），由平台判定，可能不准。 |
| `conversation_id` | 所属对话串 ID（根推文 ID），同一串的回复据此归在一起。 |
| `reply_to_user_id` | 所回复用户的数字 ID。 |
| `hashtags` | 正文里的话题标签数组，按出现顺序；没有时不出现这个字段。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_avatar_url` | 作者头像图片链接（多数平台带签名、会过期）。 |
| `author_post_count` | 作者推文总数。 |
| `author_media_count` | 作者发过的媒体数。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `mentions` | 正文里 @ 到的用户名。 |
| `author_banner_url` | 作者主页横幅图链接。 |
| `media` | 推文图片 / 视频：type（photo / video / animated_gif）、url（图片或视频封面）、width、height、duration_sec（视频秒数）、video_url（码率最高的 mp4）。 |

实测还返回了 `quote_count`、`is_reply`、`is_pinned`、`reply_to_id`、`reply_to`、`author_is_verified`、`author_following_count`、`author_created_at`、`author_bio`，接口文档里还没有它们的中文说明，表里没列。

完整参数和字段：<https://everyinfra.com/twitter-api/comments?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

#### `profile`（主页或对象详情）

| 字段 | 含义 |
|---|---|
| `user_id` | 用户在原平台的唯一 ID。 |
| `username` | 用户名（@handle）。 |
| `display_name` | 显示名，可能与 username 不同。 |
| `bio` | 个人简介，账号自己填写的文本。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `follower_count` | 粉丝数。 |
| `following_count` | 关注数。 |
| `post_count` | 发布内容总数。 |
| `is_verified` | 是否为平台认证账号（蓝V等）。 |
| `location` | 地理位置描述，原文透传，格式随平台而异。 |
| `avatar_url` | 头像图片链接。 |
| `created_at` | 创建时间，格式同 posted_at。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/twitter-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

#### `user_posts`（用户内容）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `like_count` | 点赞数。 |
| `retweet_count` | 转发数。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `view_count` | 浏览/播放数。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_url` | 作者在原平台的主页链接。 |
| `author_follower_count` | 作者粉丝数。 |
| `bookmark_count` | 书签（收藏）数。 |
| `language` | 内容语言代码（如 zh、en），由平台判定，可能不准。 |
| `conversation_id` | 所属对话串 ID（根推文 ID），同一串的回复据此归在一起。 |
| `is_quote` | 是否引用推文。 |
| `links` | 正文里的外链（展开后的完整网址）。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_avatar_url` | 作者头像图片链接（多数平台带签名、会过期）。 |
| `author_post_count` | 作者推文总数。 |
| `author_media_count` | 作者发过的媒体数。 |
| `author_banner_url` | 作者主页横幅图链接。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `media` | 推文图片 / 视频：type（photo / video / animated_gif）、url（图片或视频封面）、width、height、duration_sec（视频秒数）、video_url（码率最高的 mp4）。 |
| `reply_to_user_id` | 所回复用户的数字 ID。 |
| `hashtags` | 正文里的话题标签数组，按出现顺序；没有时不出现这个字段。 |
| `mentions` | 正文里 @ 到的用户名。 |

实测还返回了 `quote_count`、`is_reply`、`is_pinned`、`author_bio`、`author_is_verified`、`author_following_count`、`author_created_at`、`reply_to_id`、`reply_to`，接口文档里还没有它们的中文说明，表里没列。

完整参数和字段：<https://everyinfra.com/twitter-api/user_posts?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### 常见问题

**调用时要不要提供 X (Twitter) 账号或 Cookie？**

不用，请求头带 `Authorization: Bearer` 和 API Key 就能调，请求体写 `platform`、`action` 和能力参数。不用扫码、维护登录状态，也不用开浏览器。

**怎么收费？失败了收不收钱？有免费额度吗？**

按调用次数计费，每千次 $0.56 起。失败、空结果、参数错误和鉴权失败都不收费。新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见定价页 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

**能把 X (Twitter) 接口接进 Claude、Cursor 吗？**

能，远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key，不用装本地程序。Claude、Cursor、ChatGPT、Claude Code 配置见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>。Agent 能自己搜 X (Twitter) 内容、读评论、查账号。

**用 X (Twitter) 数据要注意哪些合规问题？**

EveryInfra 服务条款要求你自行确保数据用法符合适用法律和相关平台条款，禁止用于违法、侵犯隐私或知识产权，或批量抓取用于骚扰、欺诈等恶意用途。用到昵称、头像等个人信息时，只留业务用得上的字段。

**可以拿到 X (Twitter) 的哪些数据？**

X (Twitter) 有 21 个能力，其中 20 个现在可用：关键词搜索、主页或对象详情、用户内容、单条内容、评论、热榜、粉丝列表、关注列表、媒体帖子、回复帖子、转推用户、按 ID 批量查资料、账号所在地与改名记录、是否关注、社群资料、社群搜索、用户搜索、视频口播文稿、推文自串、社群帖子。每个能力的参数和返回字段见平台页 <https://everyinfra.com/twitter-api?utm_source=github&utm_medium=example_repo&utm_campaign=twitter-api>

### 实测记录

发布前用本仓的代码对线上接口跑过一遍，命令就是「快速开始」里的 5 条。

| 命令 | 时间（新加坡时间） | 返回条数 | 扣费 |
|---|---|---|---|
| `python main.py search "camping gear" --out posts.csv` | 2026-11-21 09:26 | 25 | $0.000792 |
| `python main.py post <post_id> --out post.json` | 2026-11-21 09:26 | 1 | $0.000556 |
| `python main.py replies <post_id> --out replies.csv` | 2026-11-21 09:26 | 14 | $0.000556 |
| `python main.py user <username>` | 2026-11-21 09:27 | 1 | $0.000556 |
| `python main.py posts <username> --out user_posts.csv` | 2026-11-21 09:27 | 20 | $0.000556 |

`post` 返回的一条（正文截到 60 字，作者字段没放进来）：

```json
{
  "id": "887453194909044736",
  "text": "Watch #AmazingRaceCanada &amp; reply with 3 camping items se…",
  "like_count": 28,
  "retweet_count": 10,
  "reply_count": 52,
  "view_count": 0,
  "posted_at": "2017-07-18T23:25:04+00:00",
  "quote_count": 5,
  "bookmark_count": 0,
  "language": "en"
}
```

## License

MIT
