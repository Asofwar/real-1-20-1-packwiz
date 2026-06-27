from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import sys


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Failure:
    path: str
    message: str


def item_id(value: object) -> str | None:
    if isinstance(value, dict):
        item = value.get("item")
        if isinstance(item, str):
            return item
    return None


def validate_recipe(path: Path) -> list[Failure]:
    rel = path.relative_to(ROOT).as_posix()
    data = json.loads(path.read_text(encoding="utf-8"))
    recipe_type = data.get("type")
    result_item = item_id(data.get("result"))

    failures: list[Failure] = []

    if recipe_type == "computercraft:turtle":
        if result_item not in {"computercraft:turtle_normal", "computercraft:turtle_advanced"}:
            failures.append(Failure(rel, f"computercraft:turtle must output a turtle item, got {result_item!r}"))

    if recipe_type == "computercraft:turtle_overlay":
        if result_item not in {"computercraft:turtle_normal", "computercraft:turtle_advanced"}:
            failures.append(Failure(rel, f"computercraft:turtle_overlay must output a turtle item, got {result_item!r}"))

    if recipe_type == "computercraft:computer_upgrade":
        if result_item not in {"computercraft:computer_advanced", "computercraft:turtle_advanced"}:
            failures.append(Failure(rel, f"computercraft:computer_upgrade has unexpected result {result_item!r}"))

    if recipe_type == "computercraft:impostor_shaped":
        if result_item is None:
            failures.append(Failure(rel, "computercraft:impostor_shaped is missing result.item"))

    return failures


def main() -> int:
    failures: list[Failure] = []
    for path in ROOT.rglob("*.json"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if '"type": "computercraft:' not in text:
            continue
        failures.extend(validate_recipe(path))

    if failures:
        print("Recipe sanity validation failed:")
        for failure in failures:
            print(f"- {failure.path}: {failure.message}")
        return 1

    print("Recipe sanity validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
