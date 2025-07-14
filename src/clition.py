import sys
from page import create_page, rename_page, remove_page, add_data_to_page, add_tags_to_page, show_page, edit_page_content
from localization import tr
from search import search_notes

args = sys.argv[1:]

def print_help():
    print(tr("usage"))
    print(tr("available_commands"))
    print(f"  --create <title>             {tr('create')}")
    print(f"  --rename <old> <new>         {tr('rename')}")
    print(f"  --remove <title|id>          {tr('remove')}")
    print(f"  <title|id> --add <text>      {tr('add')}")
    print(f"  <title|id> --tags <tags...>  {tr('tags')}")
    print(f"  <title|id> --show            {tr('show')}")
    print(f"  <title|id> --edit            {tr('edit')}")
    print(f"  --search <query>             {tr('search')}")
    print(f"  --all                        {tr('show_all')}")
    print(f"  -h, --help                   {tr('help')}")

if len(args) == 0 or args[0] in ("-h", "--help"):
    print_help()

elif args[0] in ("--create",):
    if len(args) >= 2:
        create_page(" ".join(args[1:]))
    else:
        print(tr("no_title"))

elif args[0] in ("--rename",):
    if len(args) >= 3:
        rename_page(args[1], " ".join(args[2:]))
    else:
        print(tr("need_old_new"))

elif args[0] in ("--remove",):
    if len(args) >= 2:
        remove_page(args[1])
    else:
        print(tr("no_remove"))

elif args[0] in ("--all",):
    # Показывает все заметки (эквивалент поиска по "*")
    from search import search_notes
    search_notes("*")

elif args[0] in ("--search",):
    if len(args) >= 2:
        search_notes(" ".join(args[1:]))
    else:
        print(tr("incomplete"))
        print_help()

elif len(args) >= 2:
    page_id = args[0]
    if args[1] == "--add" and len(args) >= 3:
        add_data_to_page(page_id, " ".join(args[2:]))
    elif args[1] == "--tags" and len(args) >= 3:
        add_tags_to_page(page_id, " ".join(args[2:]))
    elif args[1] == "--show":
        show_page(page_id)
    elif args[1] == "--edit":
        edit_page_content(page_id)
    else:
        print(tr("unknown_command"))
        print_help()
else:
    print(tr("incomplete"))
    print_help()
