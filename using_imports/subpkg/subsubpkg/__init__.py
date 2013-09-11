# using_import/subpkg/subsubpkg/__init__.py
#
# Here we import everything from modules in this package that we want to
# public above

from using_imports.subpkg.subsubpkg.submodule import (
    from_submodule,
)
