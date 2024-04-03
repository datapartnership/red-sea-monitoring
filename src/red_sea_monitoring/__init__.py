from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("red-sea-monitoring")
except PackageNotFoundError:
    # package is not installed
    pass
