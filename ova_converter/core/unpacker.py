import tarfile
from pathlib import Path


def extract_ova(ova_path: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(ova_path) as tar:
        tar.extractall(path=out_dir)

    # Find first .vmdk
    vmdks = list(out_dir.glob("*.vmdk"))
    if not vmdks:
        # Some OVAs have nested directories
        for p in out_dir.rglob("*.vmdk"):
            vmdks.append(p)
    if not vmdks:
        raise FileNotFoundError("No .vmdk found in extracted OVA")
    return vmdks[0]