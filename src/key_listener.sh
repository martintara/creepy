#!/bin/bash

# Function to run git pull
pull_code() {
    echo "Running git pull..."
    git -C ~/creepy/src pull
}


# Function to run the Python script
run_python_script() {
    echo "Running python main.py..."
    python3 ~/creepy/src/main.py
}

echo "Press 'p' to run git pull, space to run python main.py, or 'q' to quit."

# Continuous loop to listen for key presses
while true; do
    read -n1 -s key  # Read a single key press (-n1) silently (-s)

    if [[ $key == "p" ]]; then
        pull_code
    elif [[ $key == " " ]]; then
        run_python_script
    elif [[ $key == "q" ]]; then
        echo "Quitting..."
        break
    else
        echo "Invalid key. Press 'p' for git pull, 'r' to restore files, space to run Python script, or 'q' to quit."
    fi
done

