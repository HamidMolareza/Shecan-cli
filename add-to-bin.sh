#!/bin/bash

success_message() {
  echo "You can use shecan as follows:"
  echo "shecan --help"
}

python_file="main.py"
if [ ! -f "$python_file" ]; then
  echo "Can not find python: $python_file"
  exit 1
fi

output_file="/usr/bin/shecan"
if [ -f "$output_file" ]; then
  success_message
  exit 0
fi

if chmod +x "$python_file" && sudo ln -sr "$python_file" "$output_file"; then
  success_message
else
  echo "Operation failed with code $?"
  exit $?
fi
