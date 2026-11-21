"""X (Twitter) API 示例（X / Twitter API in Python）。

  python main.py search "camping gear" --out posts.csv # 按关键词搜帖子 / search posts
  python main.py post <post_id> --out post.json        # 单条帖子 / one post
  python main.py replies <post_id> --out replies.csv   # 帖子下的回复 / replies
  python main.py user <username>                       # 账号资料 / account profile
  python main.py posts <username> --out user_posts.csv # 账号发布的帖子 / an account's posts
"""
import argparse

from everyinfra import fetch, report

SORTS = ["latest"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", help="按关键词搜帖子 / search posts by keyword")
    s.add_argument("keyword")
    s.add_argument("--sort", choices=SORTS, help="latest 表示最新优先 / latest for newest first")
    po = sub.add_parser("post", help="单条帖子 / one post")
    po.add_argument("id")
    r = sub.add_parser("replies", help="帖子下的回复 / replies to one post")
    r.add_argument("id")
    u = sub.add_parser("user", help="账号资料 / account profile")
    u.add_argument("username")
    pos = sub.add_parser("posts", help="账号发布的帖子 / an account's posts")
    pos.add_argument("username")
    for x in (s, po, r, u, pos):
        x.add_argument("--out", help="存成 .csv 或 .json / write .csv or .json")
    a = p.parse_args()

    if a.cmd == "search":
        params = {"keyword": a.keyword, **({"sort": a.sort} if a.sort else {})}
        rows, charged = fetch("search", params)
    elif a.cmd == "post":
        rows, charged = fetch("post", {"id": a.id})
    elif a.cmd == "replies":
        rows, charged = fetch("comments", {"id": a.id})
    elif a.cmd == "user":
        rows, charged = fetch("profile", {"username": a.username})
    else:
        rows, charged = fetch("user_posts", {"username": a.username})
    report(rows, charged, a.out)


if __name__ == "__main__":
    main()
