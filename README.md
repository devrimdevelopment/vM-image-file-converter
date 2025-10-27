# vM-image-file-converter


Ein erweiterbares Tool zum Herunterladen, Entpacken und Konvertieren von OVA/OVF-Images in verschiedene virtuelle Festplattenformate (z. B. VHDX, QCOW2, VDI).


## Ziele
- Modularer Provider-Ansatz: neue Images (FydeOS, Ubuntu, etc.) als Provider-Plugins
- Unterstützte Ausgabeformate: vhdx, vhd, qcow2, vdi, raw
- CI: GitHub Actions Workflow zum automatischen Bauen


## Quickstart (lokal)
Voraussetzungen: Python 3.10+, qemu-img in PATH


```bash
python -m venv .venv
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate # Windows PowerShell
pip install -r requirements.txt


# Beispiel: FydeOS -> vhdx
python -m ova_converter.cli fydeos --target vhdx --workdir output

Die Pipeline (.github/workflows/build.yml) bietet einen workflow_dispatch-Trigger mit Eingaben provider und target.

Erweiterungen
- Mehr Provider hinzufügen unter ova_converter/providers
- Upload als GitHub Release Asset
- Checksummenprüfung