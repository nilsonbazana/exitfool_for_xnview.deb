#!/bin/bash
# Filter out literal "%f" arguments
clean_args=()
for arg in "$@"; do
  if [ "$arg" != "%f" ]; then
    clean_args+=("$arg")
  fi
done

/usr/bin/python3 /home/sep2025/metafixer2.py "${clean_args[@]}"
