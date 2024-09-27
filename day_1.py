# This file is part of my solutions for Advent of Code 2018.
# Copyright (C) 2024  Luka Berkers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from pathlib import Path
from typing import Optional

from utils import INPUT_DIR

_logger = logging.getLogger(__name__)

_FREQUENCY_CHANGES_FILE_NAME: Path = INPUT_DIR / 'day_1.txt'


def read_frequency_changes() -> list[int]:
    """
    Reads frequency changes from the input file and returns them as a list of integers.

    Returns:
        list[int]: A list of integer frequency changes.

    Raises:
        OSError: If the file cannot be opened or read.

    """
    frequency_changes = list[int]()

    try:
        with _FREQUENCY_CHANGES_FILE_NAME.open() as frequency_changes_file:
            for line in frequency_changes_file:
                frequency_changes.append(int(line))
    except OSError as error:
        _logger.error(error)
        raise

    return frequency_changes


def apply_frequency_changes(frequency_changes: list[int]) -> int:
    """
    Applies a list of frequency changes, starting from zero, to calculate the resulting frequency.

    Args:
        frequency_changes (list[int]): A list of integer frequency changes.

    Returns:
        int: The resulting frequency after applying all the changes.
    """
    return sum(frequency_changes)


def find_first_repeated_frequency(
        frequency_changes: list[int],
        current_frequency: int = 0,
        frequencies_encountered: Optional[set[int]] = None
) -> int:
    """
    Find the first frequency encountered a second time when applying a list of frequency changes.

    This function keeps
    applying the list of frequency changes until a repeated frequency is encountered.
    If the list of frequency changes never generates a repeated frequency,
    this function will recurse until the recursion depth limit is reached.

    Args:
        frequency_changes: List of integers representing changes in frequency.
        current_frequency (optional): The starting frequency value (default is 0).
        frequencies_encountered (optional):
            A set of frequencies encountered so far
            (default is a set containing only the starting frequency).

    Returns:
        The first frequency value that is reached twice.

    Raises:
        RecursionError: If the list of frequency changes never generates a repeated frequency.
    """
    if frequencies_encountered is None or not frequencies_encountered:
        frequencies_encountered = {current_frequency}

    for frequency_change in frequency_changes:
        current_frequency += frequency_change

        if current_frequency in frequencies_encountered:
            return current_frequency

        frequencies_encountered.add(current_frequency)

    return find_first_repeated_frequency(
        frequency_changes, current_frequency, frequencies_encountered
    )
