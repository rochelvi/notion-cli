import os

def get_lang():
    lang = os.environ.get("LANG", "en").lower()
    if lang.startswith("ru"):
        return "ru"
    return "en"

MESSAGES = {
    "ru": {
        "usage": "Использование: clition <команда>",
        "available_commands": "Доступные команды:",
        "create": "Создать страницу",
        "rename": "Переименовать страницу",
        "remove": "Удалить страницу",
        "add": "Добавить текст в страницу",
        "tags": "Добавить теги (через пробел)",
        "show": "Показать содержимое и теги",
        "help": "Показать справку",
        "show_all": "Показать все страницы",
        "search": "Поиск по названию, тегам и содержимому",
        "no_title": "Не указано имя страницы.",
        "need_old_new": "Нужно указать старое и новое имя.",
        "no_remove": "Не указано, какую страницу удалить.",
        "unknown_command": "Неизвестная команда или недостающие аргументы.",
        "incomplete": "Неполная команда.",
        "already_exists": "Страница с названием '{title}' уже существует.",
        "created": "Создана страница '{title}' с ID {id}.",
        "not_found": "Страница '{key}' не найдена.",
        "search_results": "Результаты поиска:",
        "search_empty": "Нет результатов для запроса '{search_request}'.",
        "renamed": "Страница переименована в '{new_title}'.",
        "confirm_remove": "Вы действительно хотите удалить страницу '{title}' (ID: {id})? [y/N]: ",
        "remove_cancel": "Удаление отменено.",
        "removed": "Страница '{title}' удалена.",
        "added_text": "Текст добавлен в страницу '{title}'.",
        "added_tags": "Добавлены теги: {tags}.",
        "page": "\nСтраница: {title} (ID: {id})",
        "tags_list": "Теги: {tags}",
        "content": "Содержимое:",
        "edit": "Редактировать содержимое страницы во внешнем редакторе",
    },
    "en": {
        "usage": "Usage: clition <command>",
        "available_commands": "Available commands:",
        "create": "Create a page",
        "rename": "Rename a page",
        "remove": "Remove a page",
        "add": "Add text to page",
        "tags": "Add tags (space separated)",
        "show": "Show content and tags",
        "help": "Show help",
        "show_all": "Show all pages",
        "search": "Search by title, tags, and content",
        "no_title": "No page title specified.",
        "need_old_new": "Old and new name required.",
        "no_remove": "No page specified to remove.",
        "unknown_command": "Unknown command or missing arguments.",
        "incomplete": "Incomplete command.",
        "already_exists": "Page with title '{title}' already exists.",
        "created": "Page '{title}' created with ID {id}.",
        "not_found": "Page '{key}' not found.",
        "search_results": "Search results:",
        "search_empty": "No results for query '{search_request}'.",
        "renamed": "Page renamed to '{new_title}'.",
        "confirm_remove": "Are you sure you want to remove page '{title}' (ID: {id})? [y/N]: ",
        "remove_cancel": "Remove cancelled.",
        "removed": "Page '{title}' removed.",
        "added_text": "Text added to page '{title}'.",
        "added_tags": "Tags added: {tags}.",
        "page": "\nPage: {title} (ID: {id})",
        "tags_list": "Tags: {tags}",
        "content": "Content:",
        "edit": "Edit page content in external editor",
    }
}

def tr(key, **kwargs):
    lang = get_lang()
    msg = MESSAGES.get(lang, MESSAGES["en"]).get(key, MESSAGES["en"].get(key, key))
    return msg.format(**kwargs)