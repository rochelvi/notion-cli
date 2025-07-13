import re
from localization import tr
from page import load_notes

def search_notes(query):
    """
    Ищет заметки по названию, тегам и содержимому.
    """
    data = load_notes()
    query_lower = query.lower()
    results = []
    for note in data["notes"]:
        title_match = query_lower in note["title"].lower()
        tags_match = any(query_lower in tag.lower() for tag in note.get("tags", []))
        content_match = query_lower in note.get("content", "").lower()
        if title_match or tags_match or content_match:
            results.append(note)
    if not results:
        print(tr("search_empty", search_request=query))
        return
    for note in results:
        print(tr("search_results", title=note["title"], id=note["id"]))
        print("-" * 40)
        print(tr("page", title=note["title"], id=note["id"]))
        print(tr("tags_list", tags=', '.join(note.get('tags', []))))
        print(tr("content"))
        print(note.get("content", ""))
        