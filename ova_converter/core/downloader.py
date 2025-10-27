from pathlib import Path
import requests
from tqdm import tqdm


def download(url: str, out_dir: Path, filename: str | None = None) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    if filename is None:
        filename = url.split("/")[-1]
    out_path = out_dir / filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        with open(out_path, "wb") as f, tqdm(total=total, unit_scale=True, unit="B") as bar:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    return out_path