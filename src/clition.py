import sys
from page import create_page, rename_page, remove_page, add_data_to_page, add_tags_to_page, show_page

args = sys.argv[1:]

def print_help():
    print("Usage: clition <command>")
    print("Available commands:")
    print("  page -c|--create <title>          Создать страницу")
    print("  page -rn|--rename <old> <new>     Переименовать страницу")
    print("  page -rm|--remove <title|id>      Удалить страницу")
    print("  page <title|id> -add <text>       Добавить текст в страницу")
    print("  page <title|id> -tags <tags...>   Добавить теги (через пробел)")
    print("  page <title|id> -show             Показать содержимое и теги")
    print("  -h, --help                        Показать справку")

if len(args) == 0 or args[0] in ("-h", "--help"):
    print_help()

elif args[0] == "page":
    if len(args) < 2:
        print("Не указано действие для page.")
        print_help()
    elif args[1] in ("-c", "--create"):
        if len(args) >= 3:
            create_page(" ".join(args[2:]))
        else:
            print("Не указано имя страницы.")
    elif args[1] in ("-rn", "--rename"):
        if len(args) >= 4:
            rename_page(args[2], " ".join(args[3:]))
        else:
            print("Нужно указать старое и новое имя.")
    elif args[1] in ("-rm", "--remove"):
        if len(args) >= 3:
            remove_page(args[2])
        else:
            print("Не указано, какую страницу удалить.")
    elif len(args) >= 3:
        if args[2] == "-add":
            add_data_to_page(args[1], " ".join(args[3:]))
        elif args[2] == "-tags":
            add_tags_to_page(args[1], " ".join(args[3:]))
        elif args[2] == "-show":
            show_page(args[1])
        else:
            print(f"Неизвестная подкоманда: {args[2]}")
            print_help()
    else:
        print("Неполная команда.")
        print_help()
else:
    print(f"Неизвестная команда: {args[0]}")
    print_help()
