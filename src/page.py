import json
import os
import tempfile
import subprocess
from localization import tr

NOTES_FILE = "notion_data.json"

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump({"notes": []}, f, ensure_ascii=False, indent=4)

def load_notes():
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(data):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def find_note(data, key):
    for note in data["notes"]:
        if str(note["id"]) == key or note["title"].lower() == key.lower():
            return note
    return None

def create_page(title):
    data = load_notes()
    if any(note["title"].lower() == title.lower() for note in data["notes"]):
        print(tr("already_exists", title=title))
        return
    new_id = max([note["id"] for note in data["notes"]], default=0) + 1
    data["notes"].append({
        "id": new_id,
        "title": title,
        "content": "",
        "tags": []
    })
    save_notes(data)
    print(tr("created", title=title, id=new_id))

def rename_page(key, new_title):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return
    note["title"] = new_title
    save_notes(data)
    print(tr("renamed", new_title=new_title))

def remove_page(key):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return

    confirm = input(tr("confirm_remove", title=note["title"], id=note["id"])).strip().lower()
    if confirm != 'y':
        print("Удаление отменено.")
        return

    data["notes"] = [n for n in data["notes"] if n != note]
    save_notes(data)
    print(tr("removed", title=note["title"]))

def add_data_to_page(key, new_content):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return
    note["content"] += new_content
    save_notes(data)
    print(tr("added_text", title=note["title"]))

def add_tags_to_page(key, tags_str):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return
    tags = tags_str.strip().split()
    for tag in tags:
        if tag not in note["tags"]:
            note["tags"].append(tag)
    save_notes(data)
    print(tr("added_tags", tags=' '.join(tags)))

def show_page(key):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return
    print(tr("page", title=note["title"], id=note["id"]))
    print(tr("tags", tags=', '.join(note.get('tags', []))))
    print(tr("content"))
    print(note['content'])

def edit_page_content(key):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(tr("not_found", key=key))
        return

    editor = os.environ.get("EDITOR", "nano")
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tf:
        tf.write(note["content"])
        tf.flush()
        subprocess.call([editor, tf.name])
        tf.seek(0)
        new_content = tf.read()

    note["content"] = new_content
    save_notes(data)
    print(tr("added_text", title=note["title"]))
