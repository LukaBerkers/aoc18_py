import logging
from pathlib import Path

from utils import INPUT_DIR

logger = logging.getLogger(__name__)

_FREQUENCY_CHANGES_FILE_NAME: Path = INPUT_DIR / 'day_1.txt'


def read_frequency_changes() -> list[int]:
    """
    Reads frequency changes from the input file and returns them as a list of integers.

    Raises:
        OSError: If the file cannot be opened or read.

    Returns:
        list[int]: A list of integer frequency changes.
    """
    frequency_changes = list[int]()

    try:
        with _FREQUENCY_CHANGES_FILE_NAME.open() as frequency_changes_file:
            for line in frequency_changes_file:
                frequency_changes.append(int(line))
    except OSError as error:
        logger.error(error)
        raise

    return frequency_changes


def apply_frequency_changes(frequency_changes: list[int]) -> int:
    """
    Args:
        frequency_changes (list[int]): A list of integer frequency changes.

    Returns:
        int: The resulting frequency after applying all the changes.
    """
    return sum(frequency_changes)
