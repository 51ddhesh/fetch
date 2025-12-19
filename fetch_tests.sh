#!/bin/bash

"""
!! SET HARDCODED PATHS HERE !!
"""
CP_HOME="~/codeforces"
SCRIPTS_DIR="$CP_HOME/scripts"
VENV_DIR="$SCRIPTS_DIR/.venv"
PYTHON_EXEC="$VENV_DIR/bin/python"
PYTHON_SCRIPT="$SCRIPTS_DIR/fetch.py"
REQUIREMENTS="$SCRIPTS_DIR/requirements.txt"

# --- VENV CHECK & SETUP ---
# We check if the venv python executable exists. 
# If not, we create the venv and install requirements once.
if [ ! -f "$PYTHON_EXEC" ]; then
    echo "Initializing tools environment in $VENV_DIR..."
    
    # Create venv
    python3 -m venv "$VENV_DIR" || { echo "Error: Failed to create venv"; exit 1; }
    
    # Install dependencies
    echo "Installing dependencies..."
    "$PYTHON_EXEC" -m pip install --upgrade pip -q
    "$PYTHON_EXEC" -m pip install -r "$REQUIREMENTS" -q || { echo "Error: Failed to install dependencies"; exit 1; }
    
    echo "Environment ready."
fi

if [ "$1" == "-cf" ]; then
    MODE="contest"
    [[ "$2" == "-p" ]] && MODE="problemset"
    
    CONTEST_ID="$3"
    PROBLEM_ID="$4"

    # Execute the python script using the venv python
    # It will write the test cases to your CURRENT directory
    "$PYTHON_EXEC" "$PYTHON_SCRIPT" "$CONTEST_ID" "$PROBLEM_ID" --mode "$MODE"
else
    echo "Usage: $0 -cf -[c|p] <contest> <problem>"
    echo "Example: $0 -cf -c 1950 A"
    exit 1
fi
