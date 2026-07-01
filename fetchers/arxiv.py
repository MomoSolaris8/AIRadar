import feedparser
from urllib.parse import urlencode

ARXIV_BASE_URL = 'https://export.arxiv.org/api/query'


def fetch_arxiv_items(limit=5):
    params = {
        'search_query': 'cat:cs.AI OR cat:cs.CL OR cat:cs.LG',
        'start': 0,
        'max_results': limit,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }

    url = f'{ARXIV_BASE_URL}?{urlencode(params)}'

    feed = feedparser.parse(url)

    items = []

    for entry in feed.entries:
        items.append({
            'id': entry.id,
            'source': 'arxiv',
            'title': entry.title.replace('\n', ' ').strip(),
            'url': entry.link,
            'author': ', '.join(author.name for author in entry.authors),
            'score': 0,
            'comments_count': 0,
            'raw': entry,
        })

    return items
