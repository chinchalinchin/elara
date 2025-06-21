#!/bin/bash

# Check for pypirc file or TWINE_PASSWORD
if [ ! -f ~/.pypirc ] && [ -z "$TWINE_PASSWORD" ]; then
  echo "Error: PyPi credentials not found."
  echo "Please create a ~/.pypirc file or set the TWINE_PASSWORD environment variable."
  exit 1
fi

# Build the package
echo "Building elara..."
python3 -m build

# Upload to PyPi
echo "Uploading to PyPi..."
python3 -m twine upload dist/*

echo "Successfully uploaded elara to PyPi!"