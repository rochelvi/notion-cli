import json
import os
import sys

NOTES_FILE = "notion_data.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {"notes": []}
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
        print(f"Страница с названием '{title}' уже существует.")
        return
    new_id = max([note["id"] for note in data["notes"]], default=0) + 1
    data["notes"].append({
        "id": new_id,
        "title": title,
        "content": "",
        "tags": []
    })
    save_notes(data)
    print(f"Создана страница '{title}' с ID {new_id}")

def rename_page(key, new_title):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(f"Страница '{key}' не найдена.")
        return
    note["title"] = new_title
    save_notes(data)
    print(f"Страница переименована в '{new_title}'")

def remove_page(key):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(f"Страница '{key}' не найдена.")
        return

    confirm = input(f"Вы действительно хотите удалить страницу '{note['title']}' (ID: {note['id']})? [y/N]: ").strip().lower()
    if confirm != 'y':
        print("Удаление отменено.")
        return

    data["notes"] = [n for n in data["notes"] if n != note]
    save_notes(data)
    print(f"Страница '{note['title']}' удалена.")


def add_data_to_page(key, new_content):
    data = load_notes()
    note = find_note(data, key)
    if not note:
        print(f"Страница '{key}' не найдена.")
        return
    note["content"] += "\n" + new_content
    save_notes(data)
    print(f"Данные добавлены к странице '{note['title']}'")
