# notion-cli

**notion-cli** is a simple command-line note manager with tags, search, and localization (English/Russian). All data is stored locally in `~/.local/share/notion_data.json`.

## Features

- Create, rename, and delete notes
- Add text and tags to notes
- View and edit note content in your external editor (`nano`, `vim`, etc.)
- Search by title, tags, and content
- Show all notes
- Automatic interface localization (based on system language)

## Installation

### Build

```bash
./build.sh
```

### Install

- For current user:
  ```bash
  ./install.sh --user
  ```
- System-wide (requires sudo):
  ```bash
  ./install.sh
  ```

### Uninstall

```bash
./install.sh --remove
```

## Usage

```bash
clition --create "Note title"
clition --rename <old_title|id> <new_title>
clition --remove <title|id>
clition <title|id> --add "Text"
clition <title|id> --tags tag1 tag2
clition <title|id> --show
clition <title|id> --edit
clition --search <query>
clition --all
clition --help
```

- To show all notes:
  ```bash
  clition --all
  ```
  or
  ```bash
  clition --search '*'
  ```

- To edit note content in your external editor:
  ```bash
  clition <title|id> --edit
  ```
  By default, the editor from the `EDITOR` environment variable is used (e.g., `nano`).

## Data Storage

All notes are stored in:
```
~/.local/share/notion_data.json
```

## Localization

The interface language is automatically detected from the `LANG` environment variable. If translation is unavailable, English is used.

## Dependencies

- Python 3.x
- [pyinstaller](https://pypi.org/project/pyinstaller/) (for building)

## License

MIT

---

**This project is designed for local note management and does not require nor communicate with any external servers.**