from pathlib import Path

from utils import INPUT_DIR

_FREQUENCY_CHANGES_FILE_NAME: Path = INPUT_DIR / "day_1.txt"


def read_frequency_changes() -> list[int]:
    frequency_changes = list[int]()

    with _FREQUENCY_CHANGES_FILE_NAME.open() as frequency_changes_file:
        for line in frequency_changes_file:
            frequency_changes.append(int(line))

    return frequency_changes


def apply_frequency_changes(frequency_changes: list[int]) -> int:
    return sum(frequency_changes)
