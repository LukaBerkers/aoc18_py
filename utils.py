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
from typing import Callable, TypeVar

_logger = logging.getLogger(__name__)

INPUT_DIR: Path = Path("input")

T = TypeVar('T')


def read_input_file(input_file_path: Path, line_parser: Callable[[str], T]) -> list[T]:
    """
    Reads an input file and parses each line.

    Args:
        input_file_path: The path to the input file to be read.
        line_parser:
            A callable that takes a string
            (line from the file) and returns a parsed object of type T.

    Returns:
        A list of objects parsed from each line in the input file.

    Raises:
        OSError: If the file cannot be opened or read.
    """
    results = list[T]()

    try:
        with input_file_path.open() as input_file:
            for line in input_file:
                results.append(line_parser(line))
    except OSError as error:
        _logger.error(error)
        raise

    return results
