"""
Module with invoke tasks
"""

import invoke

import {{ cookiecutter.source_directory_name }}.invoke.host


# Default invoke collection
ns = invoke.Collection()

# Add collections defined in other files
ns.add_collection({{ cookiecutter.source_directory_name }}.invoke.host)
