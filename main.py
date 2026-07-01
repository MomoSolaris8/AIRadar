from fetchers.hackernews import fetch_hackernews_items
from fetchers.arxiv import fetch_arxiv_items
from fetchers.github import fetch_github_items
from notifier.email_sender import send_email


# def print_items(title, items):
#     print(title)
#
#     for item in items:
#         print(item['title'])
#         print(item['url'])
#         print(f"score: {item['score']}")
#         print()

def format_items(title, items):
    lines = [title, '']

    for item in items:
        lines.append(item['title'])
        lines.append(item['url'])
        lines.append(f"score: {item['score']}")
        lines.append('')

    return '\n'.join(lines)


def main():
    hackernews_items = fetch_hackernews_items(limit=20, output_limit=10)
    arxiv_items = fetch_arxiv_items(limit=5)
    github_items = fetch_github_items(limit=5)

    body_parts = [
        format_items('HackerNews items:', hackernews_items),
        format_items('ArXiv items:', arxiv_items),
        format_items('GitHub items:', github_items),
    ]

    body = '\n\n'.join(body_parts)

    send_email(
        subject='AI Radar Daily Digest',
        body=body,
    )

    print('email sent')


# def main():
# hackernews_items = fetch_hackernews_items(limit=20, output_limit=10)
# print_items('hackernews items:', hackernews_items)
#
# arxiv_items = fetch_arxiv_items(limit=5)
# print_items('arxiv items:', arxiv_items)
#
# github_items = fetch_github_items(limit=5)
# print_items('github items:', github_items)


if __name__ == "__main__":
    main()
