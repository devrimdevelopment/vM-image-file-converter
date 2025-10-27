import subprocess
from pathlib import Path


def convert_image(vmdk_path: Path, out_dir: Path, target_format: str = "vhdx") -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / (vmdk_path.stem + "." + target_format)
    cmd = [
        "qemu-img", "convert",
        "-f", "vmdk",
        "-O", target_format,
        str(vmdk_path), str(target)
    ]
    subprocess.run(cmd, check=True)
    return target