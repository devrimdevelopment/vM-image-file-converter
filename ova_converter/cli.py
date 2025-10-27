"""CLI entrypoint for vM-image-file-converter"""
import argparse
from pathlib import Path
from ova_converter.core import downloader, unpacker, converter
from ova_converter.providers import fydeos, generic

PROVIDERS = {
    "fydeos": fydeos,
    "generic": generic,
}


def main():
    parser = argparse.ArgumentParser(description="Universal OVA → Disk converter")
    parser.add_argument("provider", choices=PROVIDERS.keys(), help="Provider to use")
    parser.add_argument("--target", default="vhdx", help="Target disk format (vhdx, qcow2, vdi, raw)")
    parser.add_argument("--workdir", default="build", help="Working directory")
    parser.add_argument("--no-download", action="store_true", help="Don't download; expect local OVA in workdir")
    args = parser.parse_args()

    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    provider = PROVIDERS[args.provider]

    if args.no_download:
        ova_path = provider.local_ova(workdir)
    else:
        ova_path = provider.fetch(workdir)

    print(f"Found OVA: {ova_path}")
    vmdk = unpacker.extract_ova(ova_path, workdir)
    out = converter.convert_image(vmdk, workdir, target_format=args.target)
    print(f"Done: {out}")


if __name__ == "__main__":
    main()