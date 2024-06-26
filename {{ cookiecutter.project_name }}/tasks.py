"""
Module with invoke tasks
"""

import invoke

import host.invoke.host
import {{ cookiecutter.source_directory_name }}.invoke.tests


# Default invoke collection
ns = invoke.Collection()

# Add collections defined in other files
ns.add_collection(host.invoke.host)
ns.add_collection({{ cookiecutter.source_directory_name }}.invoke.tests)
