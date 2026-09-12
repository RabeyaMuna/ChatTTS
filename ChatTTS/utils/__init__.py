def check_all_assets(*args, **kwargs):
    # Lazy import to avoid importing requests at package import time
    from .dl import check_all_assets as _check_all_assets

    return _check_all_assets(*args, **kwargs)


def download_all_assets(*args, **kwargs):
    # Lazy import to avoid importing requests at package import time
    from .dl import download_all_assets as _download_all_assets

    return _download_all_assets(*args, **kwargs)


from .gpu import select_device
from .io import FileLike, del_all, get_latest_modified_file, load_safetensors
from .log import logger
