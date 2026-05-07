import requests


OPEN_LIBRARY_SEARCH_URL = "https://openlibrary.org/search.json"


def search_open_library(query, sort_by=None, has_cover=False):
    """
    Searches Open Library for books matching the user's query.

    Args:
        query: Search term entered by the user.
        sort_by: Optional sort choice used in local result sorting.
        has_cover: If True, removes books without cover images.

    Returns:
        A dictionary with success status, results, and optional error message.
    """

    if not query:
        return {
            "success": False,
            "results": [],
            "error": "Please enter a book title or author."
        }

    params = {
        "q": query,
        "limit": 20,
        "fields": ",".join([
            "key",
            "title",
            "author_name",
            "first_publish_year",
            "cover_i",
            "isbn",
            "subject"
        ])
    }

    try:
        response = requests.get(
            OPEN_LIBRARY_SEARCH_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "results": [],
            "error": "The book search took too long. Please try again."
        }
    except requests.exceptions.RequestException:
        return {
            "success": False,
            "results": [],
            "error": "Book search is currently unavailable. Please try again later."
        }

    data = response.json()
    books = data.get("docs", [])

    results = []

    for book in books:
        author_names = book.get("author_name", [])
        isbn_list = book.get("isbn", [])

        result = {
            "open_library_key": book.get("key", ""),
            "title": book.get("title", "Unknown title"),
            "author": ", ".join(author_names) if author_names else "Unknown author",
            "first_publish_year": book.get("first_publish_year"),
            "cover_id": book.get("cover_i"),
            "isbn": isbn_list[0] if isbn_list else "",
        }

        if has_cover and not result["cover_id"]:
            continue

        results.append(result)

    if sort_by == "author":
        results.sort(key=lambda item: item["author"].lower())
    elif sort_by == "title":
        results.sort(key=lambda item: item["title"].lower())

    return {
        "success": True,
        "results": results,
        "error": None
    }