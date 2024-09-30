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

import utils
from utils import INPUT_DIR

_logger = logging.getLogger(__name__)

_BOX_IDS_FILE_PATH: Path = INPUT_DIR / 'day_2.txt'


def read_box_ids() -> list[str]:
    """
    Reads box IDs from the input file and returns them as a list of strings.

    Returns:
        list[str]: A list of box IDs read from the file.

    Raises:
        OSError: If the file cannot be opened or read.
    """
    return utils.read_input_file(_BOX_IDS_FILE_PATH, lambda s: s.strip())


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


def find_box_ids_that_differ_by_one_letter(box_ids: list[str]) -> Optional[str]:
    """
    Finds the common letters between two box IDs that differ by exactly one letter.

    Args:
        box_ids: A list of strings representing the box IDs.

    Returns:
        A string
        containing the letters that are common between the two box IDs which differ by exactly one
        letter at the same position.
        If no such IDs are found, returns None.
    """
    for i, id1 in enumerate(box_ids):
        for id2 in box_ids[i + 1:]:
            equal_letters = _equal_letters_from_ids(id1, id2)

            if len(equal_letters) == len(id1) - 1:
                return equal_letters

    return None


def _equal_letters_from_ids(id1: str, id2: str) -> str:
    """
    Finds the equal letters at the same positions in two box IDs.

    Args:
        id1: The first box ID to be compared for equal letters.
        id2: The second box ID to be compared for equal letters.

    Returns:
        A string containing the letters from the input strings
        that are equal at the same positions.
    """
    equal_letters = ''

    for letter1, letter2 in zip(id1, id2):
        if letter1 == letter2:
            equal_letters += letter1

    return equal_letters
