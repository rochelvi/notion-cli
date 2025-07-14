#!/bin/bash

# This script will build the project and prepare it for deployment.

echo "Creating isolated environment..."

python3 -m venv venv

echo "Setting up the virtual environment..."
source venv/bin/activate

echo "Done!"
echo "Installing dependencies..."

pip install -r requirements.txt
echo "Dependencies installed!"
echo "Building the project..."

pyinstaller --onefile src/clition.py

echo "Build complete! Now you can run ./install.sh to install the application."