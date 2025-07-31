import os
from typing import Optional


def get_default_platform() -> Optional[str]:
    if "DOCKER_DEFAULT_PLATFORM" in os.environ:
        return os.environ["DOCKER_DEFAULT_PLATFORM"]
    return None
