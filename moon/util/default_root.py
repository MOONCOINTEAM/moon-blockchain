import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("MOON_ROOT", "~/.moon/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("MOON_KEYS_ROOT", "~/.moon_keys"))).resolve()
