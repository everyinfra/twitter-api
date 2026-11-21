#!/usr/bin/env bash
# X (Twitter) API 的 curl 示例：所有能力都发到同一个地址，只换 action 和 params。
# curl examples for the X (Twitter) API: every capability uses the same URL; only action and params change.
#
#   export EVERYINFRA_API_KEY=<your API key>
#   bash examples/curl.sh search "camping gear"
#   bash examples/curl.sh post <post_id>        # search 结果里的 id / the id from a search result
#   bash examples/curl.sh comments <post_id>
#   bash examples/curl.sh profile <username>    # search 结果里的 author_username / the author_username from a search result
#   bash examples/curl.sh user_posts <username>
set -euo pipefail
: "${EVERYINFRA_API_KEY:?Set EVERYINFRA_API_KEY first: https://everyinfra.com/docs#quickstart}"
action=${1:?"usage: bash examples/curl.sh <search|post|comments|profile|user_posts> <value>"}
value=${2:?"value: a keyword, a post id or a username"}

case "$action" in
  search)               params="{\"keyword\":\"$value\"}" ;;
  post | comments)      params="{\"id\":\"$value\"}" ;;
  profile | user_posts) params="{\"username\":\"$value\"}" ;;
  *) echo "unknown action: $action (use search, post, comments, profile or user_posts)" >&2; exit 2 ;;
esac

curl -sS -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"platform\":\"twitter\",\"action\":\"$action\",\"params\":$params}"
echo
