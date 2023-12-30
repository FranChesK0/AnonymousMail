import os
from abc import ABC
from typing import Final

from dotenv import load_dotenv

root_dir: str = str(os.path.dirname(os.path.abspath(__file__))).removesuffix(f"{os.path.sep}src{os.path.sep}misc")
load_dotenv(f"{root_dir}{os.path.sep}data{os.path.sep}.env")


class Env(ABC):
    ROOT_DIR: Final[str] = root_dir
    DEBUG: Final[int] = int(os.environ.get("DEBUG", "DEBUG is undefined"))
    API: Final[str] = os.environ.get("API", "API is undefined")
