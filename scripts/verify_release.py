#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import zipfile
from pathlib import Path


EXPECTED_IMAGES = 622
EXPECTED_LABELS = "data/official/5164_gts.csv"
EXPECTED_EXAMPLE_LABELS = "examples/example_labels.csv"
ABSOLUTE_PATH_RE = re.compile(r"^(?:[A-Za-z]:[\\/]|/)")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the Pennsylvania Death Records 622 release zip.")
    parser.add_argument("--release_zip", required=True, help="Path to the release zip.")
    parser.add_argument("--sha256sums", help="Optional SHA256SUMS file containing the release zip checksum.")
    args = parser.parse_args()

    release_zip = Path(args.release_zip)
    if not release_zip.is_file():
        print(f"missing release zip: {release_zip}", file=sys.stderr)
        return 2

    if args.sha256sums:
        sums_path = Path(args.sha256sums)
        if not sums_path.is_file():
            print(f"missing sha256sums file: {sums_path}", file=sys.stderr)
            return 2
        line = sums_path.read_text(encoding="utf-8").strip().split()
        if len(line) < 2:
            print("sha256sums file is malformed", file=sys.stderr)
            return 2
        expected = line[0].lower()
        actual = sha256_file(release_zip)
        if actual != expected:
            print(f"checksum mismatch: expected {expected} got {actual}", file=sys.stderr)
            return 1

    with zipfile.ZipFile(release_zip) as z:
        names = set(z.namelist())
        if EXPECTED_LABELS not in names:
            print(f"missing official labels csv: {EXPECTED_LABELS}", file=sys.stderr)
            return 1
        if EXPECTED_EXAMPLE_LABELS not in names:
            print(f"missing example labels csv: {EXPECTED_EXAMPLE_LABELS}", file=sys.stderr)
            return 1

        img_names = sorted(n for n in names if n.startswith("images/") and n.lower().endswith(".jpg"))
        if len(img_names) != EXPECTED_IMAGES:
            print(f"expected {EXPECTED_IMAGES} images, found {len(img_names)}", file=sys.stderr)
            return 1

        with z.open(EXPECTED_LABELS) as f:
            text = (line.decode("utf-8-sig") for line in f)
            reader = csv.DictReader(text)
            rows = list(reader)
        if len(rows) != EXPECTED_IMAGES:
            print(f"expected {EXPECTED_IMAGES} label rows, found {len(rows)}", file=sys.stderr)
            return 1

        image_keys = [row["ImageFileName"] for row in rows]
        if len(image_keys) != len(set(image_keys)):
            print("duplicate ImageFileName values found in official labels", file=sys.stderr)
            return 1

        expected_image_files = {f"images/{key}.jpg" for key in image_keys}
        missing_images = sorted(expected_image_files - set(img_names))
        if missing_images:
            print(f"missing images for {len(missing_images)} labels", file=sys.stderr)
            return 1

        bad_paths = [row["image_path"] for row in rows if ABSOLUTE_PATH_RE.match(row.get("image_path", ""))]
        if bad_paths:
            print("found non-archive-relative image_path values", file=sys.stderr)
            return 1

        with z.open(EXPECTED_EXAMPLE_LABELS) as f:
            text = (line.decode("utf-8-sig") for line in f)
            example_rows = list(csv.DictReader(text))
        if not example_rows:
            print("example labels csv is empty", file=sys.stderr)
            return 1

    print("release verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
