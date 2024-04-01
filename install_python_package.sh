#!/bin/bash
# Check if package name is supplied
if [ -z "$1" ]
then
    echo "No package supplied. Usage: ./install.sh <package>"
    exit 1
fi

# Install the package
pip install $1

# Check if installation was successful
if [ $? -eq 0 ]
then
    echo "Package $1 installed successfully."
else
    echo "Failed to install package $1."
    exit 1
fi
