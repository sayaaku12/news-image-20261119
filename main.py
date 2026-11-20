#!/usr/bin/env python3
"""news-image-20261119 entrypoint.

Copies the bundled front page (entry.png, rendered with PIL for
Thursday 19 November 2026) to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Standard library only, no network, fully
deterministic: the same input bytes always produce the same output
bytes, so the grader's two runs write identical files.
"""
import hashlib
import os
import sys

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_BYTES = 1_048_576  # competition gate: image at most 1 MiB

# PNG signature: the first 8 bytes of any valid PNG file.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def source_path():
    """Absolute path of the bundled image next to this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def output_dir():
    """Output directory from the environment, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def read_source(path):
    """Read the bundled image bytes, failing loudly if absent."""
    if not os.path.isfile(path):
        raise SystemExit(f"bundled image missing: {path}")
    with open(path, "rb") as handle:
        return handle.read()


def write_output(data, directory):
    """Write the image bytes to <directory>/entry.png atomically.

    The bytes go to a temp file in the same directory first and are
    then moved into place, so a reader never sees a half-written
    entry.png, and a failed run leaves no corrupt output behind.
    """
    if len(data) > MAX_BYTES:
        raise SystemExit(
            f"bundled image too large: {len(data)} bytes > {MAX_BYTES}")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, OUTPUT_NAME)
    tmp = target + ".tmp"
    with open(tmp, "wb") as handle:
        handle.write(data)
    os.replace(tmp, target)
    return target


def main():
    data = read_source(source_path())
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("bundled image is not a PNG")
    target = write_output(data, output_dir())
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
