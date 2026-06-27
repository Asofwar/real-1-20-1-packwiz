from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX_FILES = ("index-main.toml",)
PACK_FILES = ("pack.toml",)
NORMALIZED_TEXT_FILES = (*INDEX_FILES, *PACK_FILES)


@dataclass(frozen=True)
class Failure:
    message: str


ENTRY_RE = re.compile(
    r'\[\[files\]\]\nfile = "(?P<file>[^"]+)"\nhash = "(?P<hash>[0-9a-f]+)"',
    re.MULTILINE,
)
PACK_INDEX_RE = re.compile(
    r"\[index\]\nfile = \"(?P<file>[^\"]+)\"\nhash-format = \"(?P<format>[^\"]+)\"\nhash = \"(?P<hash>[0-9a-f]+)\"",
    re.MULTILINE,
)


def has_crlf_bytes(path: Path) -> bool:
    return b"\r\n" in path.read_bytes()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def parse_index(index_path: Path) -> dict[str, str]:
    text = index_path.read_text(encoding="utf-8")
    entries: dict[str, str] = {}
    for match in ENTRY_RE.finditer(text):
        entries[match.group("file")] = match.group("hash")
    return entries


def parse_pack_index(pack_path: Path) -> tuple[str, str, str]:
    text = pack_path.read_text(encoding="utf-8")
    match = PACK_INDEX_RE.search(text)
    if not match:
        raise ValueError(f"Could not parse [index] section in {pack_path.name}")
    return match.group("file"), match.group("format"), match.group("hash")


def verify() -> list[Failure]:
    failures: list[Failure] = []

    for rel in NORMALIZED_TEXT_FILES:
        path = ROOT / rel
        if has_crlf_bytes(path):
            failures.append(Failure(f"{rel} contains CRLF line endings"))

    pw_files = sorted((ROOT / "mods").glob("*.pw.toml"))
    if not pw_files:
        failures.append(Failure("No .pw.toml files found under mods/"))
        return failures

    for path in pw_files:
        rel = path.relative_to(ROOT).as_posix()
        if has_crlf_bytes(path):
            failures.append(Failure(f"{rel} contains CRLF line endings"))

    expected_pw_hashes = {
        path.relative_to(ROOT).as_posix(): file_sha256(path) for path in pw_files
    }

    parsed_indexes: dict[str, dict[str, str]] = {}
    for index_name in INDEX_FILES:
        index_path = ROOT / index_name
        parsed = parse_index(index_path)
        parsed_indexes[index_name] = parsed
        for rel, expected_hash in expected_pw_hashes.items():
            actual_hash = parsed.get(rel)
            if actual_hash is None:
                failures.append(Failure(f"{index_name} is missing entry for {rel}"))
            elif actual_hash != expected_hash:
                failures.append(
                    Failure(
                        f"{index_name} has wrong hash for {rel}: expected {expected_hash}, got {actual_hash}"
                    )
                )

    index_main_hash = file_sha256(ROOT / "index-main.toml")
    for pack_name in PACK_FILES:
        pack_path = ROOT / pack_name
        try:
            index_file, hash_format, actual_hash = parse_pack_index(pack_path)
        except ValueError as exc:
            failures.append(Failure(str(exc)))
            continue

        if index_file != "index-main.toml":
            failures.append(
                Failure(f"{pack_name} points to {index_file} instead of index-main.toml")
            )
        if hash_format != "sha256":
            failures.append(Failure(f"{pack_name} uses hash-format {hash_format} instead of sha256"))
        if actual_hash != index_main_hash:
            failures.append(
                Failure(
                    f"{pack_name} has wrong index hash: expected {index_main_hash}, got {actual_hash}"
                )
            )

    return failures


def main() -> int:
    failures = verify()
    if failures:
        print("Packwiz verification failed:")
        for failure in failures:
            print(f"- {failure.message}")
        return 1

    print("Packwiz verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
