#!/bin/bash

function is_md5() {
    local input=$1
    if [[ $input =~ ^[a-f0-9]{32}$ ]]; then
        return 0  # Return true if input matches MD5 hash pattern
    else
        return 1  # Return false otherwise
    fi
}

# Main function
function main() {
    read -p "Input String ~# " input_string
    if is_md5 "$input_string"; then
        echo "MD5 type"
    else
        echo "Not MD5 type"
    fi
}

# Run the main function
main
