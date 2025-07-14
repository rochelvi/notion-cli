#!/bin/bash

# This script installs the necessary dependencies for the project.

if [ ! -d "dist" ]; then
    echo "Executable not found. Please run build.sh first."
    exit 1
fi

if [ "$1" == "--user" ]; then
    echo "Installing for the current user..."
    mkdir -p ~/.local/bin
    cp dist/clition ~/.local/bin/clition
    chmod +x ~/.local/bin/clition
    echo "Installation complete! You can now run 'clition'."
elif [ "$1" == "--remove" ]; then
    echo "Uninstalling..."
    rm -f ~/.local/bin/clition
    rm -f /usr/local/bin/clition
    echo "Uninstallation complete!"
    exit 0
elif [ "$1" == "--help" ]; then
    echo "Usage: install.sh [--user | --remove | --help]"
    echo "Options:"
    echo "  --user   Install for the current user  (By default, installs system-wide)"
    echo "  --remove Uninstall the application"
    echo "  --help   Show this help message"
    exit 0
else
    echo "Installing system-wide..."
    sudo cp dist/clition /usr/local/bin/clition
    sudo chmod +x /usr/local/bin/clition
    echo "Installation complete! You can now run 'clition'."
fi