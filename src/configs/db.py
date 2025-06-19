import os
from pathlib import Path

PATH_TO_DB = os.path.join(Path(__file__).absolute().parents[2], Path("data/db.db"))
PATH_TO_FILES = os.path.join(Path(__file__).absolute().parents[2], Path("data/files"))
