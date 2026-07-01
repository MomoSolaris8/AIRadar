import requests

HN_BASE_URL = "https://hacker-news.firebaseio.com/v0"
HN_ITEM_URL = 'https://news.ycombinator.com/item?id={id}'

AI_KEYWORDS = [
    'artificial intelligence',
    'llm',
    'openai',
    'anthropic',
    'agent',
    'agents',
    'machine learning',
    'deep learning',
    'gpt',
    'claude',
    'gemini',
    'rag',
    'inference',
]


def fetch_top_story_ids(limit=20):
    response = requests.get(f"{HN_BASE_URL}/topstories.json", timeout=10)
    response.raise_for_status()
    return response.json()[:limit]


def fetch_item(item_id):
    response = requests.get(f"{HN_BASE_URL}/item/{item_id}.json", timeout=10)
    response.raise_for_status()
    return response.json()


def normalize_item(raw_item):
    if raw_item is None:
        return None

    if raw_item.get('type') != 'story':
        return None

    if raw_item.get('deleted') or raw_item.get('dead'):
        return None

    title = raw_item.get('title')
    if not title:
        return None

    item_id = raw_item['id']

    return {
        'id': str(item_id),
        'source': 'Hacker News',
        'title': title,
        'url': raw_item.get('url') or HN_ITEM_URL.format(id=item_id),
        'author': raw_item.get('by'),
        'score': raw_item.get('score', 0),
        'comments_count': raw_item.get('descendants', 0),
        'raw': raw_item
    }


def is_ai_related(item):
    text = f"{item['title']} {item['url']}".lower()
    return any(keyword in text for keyword in AI_KEYWORDS)


def fetch_hackernews_items(limit=20, output_limit=10):
    story_ids = fetch_top_story_ids(limit=limit)
    items = []

    for story_id in story_ids:
        raw_item = fetch_item(story_id)
        item = normalize_item(raw_item)

        if item is None:
            continue

        items.append(item)

    items = sorted(items, key=lambda x: x['score'], reverse=True)

    return items[:output_limit]


