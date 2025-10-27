from pathlib import Path
import shutil


def ensure_executable_in_path(cmd: str) -> bool:
    return shutil.which(cmd) is not None