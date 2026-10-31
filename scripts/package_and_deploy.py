import os
import tarfile
import subprocess
import sys

BASE_DIR = r"C:\Users\Alone\Desktop\syntaxcraft.dev"
OUTPUT_DIR = os.path.join(BASE_DIR, ".output")
TAR_PATH = os.path.join(BASE_DIR, "deploy_output.tar.gz")

print(f"1. Compressing {OUTPUT_DIR} into {TAR_PATH}...")
if os.path.exists(TAR_PATH):
    os.remove(TAR_PATH)

with tarfile.open(TAR_PATH, "w:gz") as tar:
    for item in os.listdir(OUTPUT_DIR):
        full_item = os.path.join(OUTPUT_DIR, item)
        tar.add(full_item, arcname=item)

size_mb = os.path.getsize(TAR_PATH) / (1024 * 1024)
print(f"✓ Created {TAR_PATH} ({size_mb:.2f} MB)")

print("\n2. Executing deploy_to_hostinger.py...")
deploy_script = os.path.join(BASE_DIR, "deploy_to_hostinger.py")
ret = subprocess.run([sys.executable, deploy_script], cwd=BASE_DIR)
sys.exit(ret.returncode)

