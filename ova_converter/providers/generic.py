"""Generic provider: benutzt eine lokale OVA oder eine URL, die über ENV/Argument übergeben werden kann"""
from pathlib import Path
from ova_converter.core.downloader import download
import os


def fetch(out_dir: Path) -> Path:
    # Erwartet ENV VAR OVA_URL oder Datei 'image.ova' im Arbeitsverzeichnis
    url = os.getenv("OVA_URL")
    if url:
        return download(url, out_dir)
    # fallback: looks for image.ova
    candidate = out_dir / "image.ova"
    if candidate.exists():
        return candidate
    raise RuntimeError("No OVA_URL env var and no image.ova found in workdir")


def local_ova(out_dir: Path) -> Path:
    candidate = out_dir / "image.ova"
    if candidate.exists():
        return candidate
    raise FileNotFoundError("Local OVA not found: image.ova")