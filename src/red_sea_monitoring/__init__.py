from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("red-sea-monitoring")
except PackageNotFoundError:
    # package is not installed
    pass
