#!/bin/bash

# Path to the folder (you can hardcode it or pass as argument)
folder_path="E:\DevOps Practises\rename_sh"  # or use "$1" if passing folder path as an argument

# Loop through all files in the folder
for file in "$folder_path"/*; do
    # Check if it's a file (not a directory)
    if [ -f "$file" ]; then
        # Get the directory and filename
        dir=$(dirname "$file")
        base=$(basename "$file")
        new_name="pw_$base"
        
        # Rename the file
        mv "$file" "$dir/$new_name"
        echo "Renamed: $base → pw_$base"
    fi
done