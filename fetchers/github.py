import requests

GITHUB_SEARCH_URL = 'https://api.github.com/search/repositories'


def fetch_github_items(limit=5):
    params = {
        'q': 'llm stars:>1000',
        'sort': 'stars',
        'order': 'desc',
        'per_page': limit,
    }

    response = requests.get(
        GITHUB_SEARCH_URL,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    items = []

    for repo in data.get('items', []):
        items.append({
            'id': str(repo['id']),
            'source': 'github',
            'title': repo['full_name'],
            'url': repo['html_url'],
            'author': repo['owner']['login'],
            'score': repo['stargazers_count'],
            'comments_count': 0,
            'raw': repo,
        })

    return items
