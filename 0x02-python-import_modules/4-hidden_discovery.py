#!/usr/bin/python3
import hidden_4  # Import the module

if __name__ == "__main__":
    # List the names defined in the imported module that don't start with "__"
    module_names = dir(hidden_4)
    result_names = [
            name for name in module_names
            if name.isidentifier() and not name.startswith("__")
            ]

    # Sort the result names alphabetically
    result_names.sort()

    # Print the sorted result names
    for name in result_names:
        print(name)
