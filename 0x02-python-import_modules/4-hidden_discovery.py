#!/usr/bin/python3
import hidden_4  # Import the module

# List the names defined in the imported module
module_names = dir(hidden_4)
print("module_names")
for name in module_names:
    if name.isidentifier():
        print(name)
