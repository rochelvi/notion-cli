import sys
from page import create_page, rename_page, remove_page, add_data_to_page, add_tags_to_page, show_page

args = sys.argv[1:]

def print_help():
    print("Usage: clition <command>")
    print("Available commands:")
    print("  --create <title>             Создать страницу")
    print("  --rename <old> <new>         Переименовать страницу")
    print("  --remove <title|id>          Удалить страницу")
    print("  <title|id> --add <text>      Добавить текст в страницу")
    print("  <title|id> --tags <tags...>  Добавить теги (через пробел)")
    print("  <title|id> --show            Показать содержимое и теги")
    print("  -h, --help                   Показать справку")

if len(args) == 0 or args[0] in ("-h", "--help"):
    print_help()

elif args[0] in ("--create",):
    if len(args) >= 2:
        create_page(" ".join(args[1:]))
    else:
        print("Не указано имя страницы.")

elif args[0] in ("--rename",):
    if len(args) >= 3:
        rename_page(args[1], " ".join(args[2:]))
    else:
        print("Нужно указать старое и новое имя.")

elif args[0] in ("--remove",):
    if len(args) >= 2:
        remove_page(args[1])
    else:
        print("Не указано, какую страницу удалить.")

elif len(args) >= 2:
    page_id = args[0]
    if args[1] == "--add" and len(args) >= 3:
        add_data_to_page(page_id, " ".join(args[2:]))
    elif args[1] == "--tags" and len(args) >= 3:
        add_tags_to_page(page_id, " ".join(args[2:]))
    elif args[1] == "--show":
        show_page(page_id)
    else:
        print("Неизвестная команда или недостающие аргументы.")
        print_help()
else:
    print("Неполная команда.")
    print_help()
