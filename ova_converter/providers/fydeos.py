"""Simple FydeOS provider. Falls URL ändert, kann hier nur die URL angepasst werden."""
from pathlib import Path
from ova_converter.core.downloader import download

FYDEOS_URL = "https://download.fydeos.io/VM/FydeOS-VMware-latest.ova"


def fetch(out_dir: Path) -> Path:
    return download(FYDEOS_URL, out_dir, filename="fydeos-latest.ova")


def local_ova(out_dir: Path) -> Path:
    candidate = out_dir / "fydeos-latest.ova"
    if candidate.exists():
        return candidate
    raise FileNotFoundError("Local FydeOS OVA not found: fydeos-latest.ova")