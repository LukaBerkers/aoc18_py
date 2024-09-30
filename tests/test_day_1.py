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

import unittest
from typing import Optional

from hypothesis import assume, given, strategies as st

import day_1


class TestFindFirstRepeatedFrequency(unittest.TestCase):
    # pp 0, 1, 2: infeasible

    # pp 3
    @given(st.integers(), st.sets(st.integers()), st.integers(), st.integers())
    def test_terminates_after_recursing_when_frequency_has_already_been_encountered(
            self,
            current_frequency: int,
            frequencies_encountered: set[int],
            first_frequency_change: int,
            second_frequency_change: int
    ):
        # Arrange
        after_first_frequency_change = current_frequency + first_frequency_change
        after_second_frequency_change = after_first_frequency_change + second_frequency_change
        after_third_frequency_change = after_second_frequency_change + first_frequency_change
        assume(after_first_frequency_change != after_second_frequency_change)
        assume(after_first_frequency_change != after_third_frequency_change)
        assume(after_second_frequency_change != after_third_frequency_change)
        frequency_changes = [first_frequency_change, second_frequency_change]
        frequencies_encountered.discard(after_first_frequency_change)
        frequencies_encountered.discard(after_second_frequency_change)
        frequencies_encountered.add(after_third_frequency_change)

        # Act
        result = day_1.find_first_repeated_frequency(
            frequency_changes, current_frequency, frequencies_encountered
        )

        # Assert
        self.assertEqual(after_third_frequency_change, result)

    # pp 4
    @given(st.integers(), st.sets(st.integers()), st.integers(), st.integers())
    def test_keeps_applying_frequency_changes_after_list_has_been_exhausted(
            self,
            current_frequency: int,
            frequencies_encountered: set[int],
            first_frequency_change: int,
            second_frequency_change: int
    ):
        # Arrange
        after_first_frequency_change = current_frequency + first_frequency_change
        after_second_frequency_change = after_first_frequency_change + second_frequency_change
        after_third_frequency_change = after_second_frequency_change + first_frequency_change
        after_fourth_frequency_change = after_third_frequency_change + second_frequency_change
        all_frequencies_to_be_encountered = [after_first_frequency_change,
                                             after_second_frequency_change,
                                             after_third_frequency_change,
                                             after_fourth_frequency_change]
        # Assume they are all different.
        assume(
            len(all_frequencies_to_be_encountered) == len(set(all_frequencies_to_be_encountered))
        )
        frequency_changes = [first_frequency_change, second_frequency_change]
        frequencies_encountered.discard(after_first_frequency_change)
        frequencies_encountered.discard(after_second_frequency_change)
        frequencies_encountered.discard(after_third_frequency_change)
        frequencies_encountered.add(after_fourth_frequency_change)

        # Act
        result = day_1.find_first_repeated_frequency(
            frequency_changes, current_frequency, frequencies_encountered
        )

        # Assert
        self.assertEqual(after_fourth_frequency_change, result)

    # pp 5
    @given(st.integers(), st.sets(st.integers()), st.integers(), st.integers())
    def test_terminates_when_frequency_has_already_been_encountered(
            self,
            current_frequency: int,
            frequencies_encountered: set[int],
            first_frequency_change: int,
            second_frequency_change: int
    ):
        # Arrange
        after_first_frequency_change = current_frequency + first_frequency_change
        after_second_frequency_change = after_first_frequency_change + second_frequency_change
        assume(after_first_frequency_change != after_second_frequency_change)
        frequency_changes = [first_frequency_change, second_frequency_change]
        frequencies_encountered.discard(after_first_frequency_change)
        frequencies_encountered.add(after_second_frequency_change)

        # Act
        result = day_1.find_first_repeated_frequency(
            frequency_changes, current_frequency, frequencies_encountered
        )

        # Assert
        self.assertEqual(after_second_frequency_change, result)

    # pp 6, 7, 8, 9
    @given(st.integers(), st.one_of(st.sets(st.integers(), max_size=0), st.none()))
    def test_without_frequencies_encountered_no_frequency_changes_reaches_recursion_limit(
            self, current_frequency: int, frequencies_encountered: Optional[set[int]]
    ):
        # Arrange
        frequency_changes = []

        # Act, Assert
        with self.assertRaises(RecursionError):
            day_1.find_first_repeated_frequency(
                frequency_changes, current_frequency, frequencies_encountered
            )

    # pp 10, 11, 13
    @given(st.lists(st.integers(), min_size=3), st.integers(), st.sets(st.integers()))
    def test_loops_when_frequency_is_not_yet_encountered(
            self,
            frequency_changes: list[int],
            current_frequency: int,
            frequencies_encountered: set[int]
    ):
        # Arrange
        after_first_frequency_change = current_frequency + frequency_changes[0]
        after_second_frequency_change = after_first_frequency_change + frequency_changes[1]
        after_third_frequency_change = after_second_frequency_change + frequency_changes[2]
        assume(after_first_frequency_change != after_second_frequency_change)
        assume(after_second_frequency_change != after_third_frequency_change)
        frequencies_encountered.discard(after_first_frequency_change)
        frequencies_encountered.discard(after_second_frequency_change)
        frequencies_encountered.add(after_third_frequency_change)

        # Act
        result = day_1.find_first_repeated_frequency(
            frequency_changes, current_frequency, frequencies_encountered
        )

        # Assert
        self.assertEqual(after_third_frequency_change, result)

    # pp 12, 14, 15
    @given(st.integers(), st.sets(st.integers(), min_size=1))
    def test_with_frequencies_encountered_no_frequency_changes_reaches_recursion_limit(
            self, current_frequency: int, frequencies_encountered: set[int]
    ):
        # Arrange
        frequency_changes = []

        # Act, Assert
        with self.assertRaises(RecursionError):
            day_1.find_first_repeated_frequency(
                frequency_changes, current_frequency, frequencies_encountered
            )


if __name__ == '__main__':
    unittest.main()
