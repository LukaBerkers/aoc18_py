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

import day_2

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
)
_logger = logging.getLogger(__name__)


def main():
    try:
        box_ids = day_2.read_box_ids()
    except OSError:
        _logger.critical('Could not open or read the file containing the box IDs.')
        return

    equal_letters = day_2.find_box_ids_that_differ_by_one_letter(box_ids)
    if equal_letters:
        print(f'The common letters are: {equal_letters}.')
    else:
        print('No box ids found that only differ by one letter.')


if __name__ == '__main__':
    main()
