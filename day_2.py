import logging
from pathlib import Path

from utils import INPUT_DIR

_logger = logging.getLogger(__name__)

_BOX_IDS_FILE_NAME: Path = INPUT_DIR / 'day_2.txt'


def read_box_ids() -> list[str]:
    """
    Reads box IDs from the input file and returns them as a list of strings.

    Returns:
        list[str]: A list of box IDs read from the file.

    Raises:
        OSError: If the file cannot be opened or read.
    """
    box_ids = list[str]()

    try:
        with _BOX_IDS_FILE_NAME.open() as box_ids_file:
            for line in box_ids_file:
                box_ids.append(line.strip())
    except OSError as error:
        _logger.error(error)
        raise

    return box_ids


def count_box_ids_containing_a_letter_two_and_three_times(box_ids: list[str]) -> tuple[int, int]:
    """
    Finds how many box IDs have any letter twice and how many box IDs have any letter three times.

    Args:
        box_ids: A list of strings representing box IDs.

    Returns:
        A tuple containing the count of box IDs that have any letter exactly twice and the count of
        box IDs that have any letter exactly three times.
    """
    id_has_a_letter_two_times_count = 0
    id_has_a_letter_three_times_count = 0

    for box_id in box_ids:
        letter_frequencies = dict[str, int]()

        for letter in box_id:
            if letter not in letter_frequencies:
                letter_frequencies[letter] = 1
            else:
                letter_frequencies[letter] += 1

        if 2 in letter_frequencies.values():
            id_has_a_letter_two_times_count += 1
        if 3 in letter_frequencies.values():
            id_has_a_letter_three_times_count += 1

    return id_has_a_letter_two_times_count, id_has_a_letter_three_times_count
