import importlib

__all__ = ["Chat"]


def __getattr__(name):
    if name == "Chat":
        module = importlib.import_module(".core", __package__)
        return getattr(module, "Chat")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
