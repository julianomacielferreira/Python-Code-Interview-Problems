"""
The MIT License

Copyright 2025 Juliano Maciel.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from data import int_array


def binary_search_first_occurrence(array, target):
    """
        Binary search to return the first occurrence of an integer in ordered array

        Params:
            array (array): Ordered array
            target (int): Number to find its position

        Returns:
            -1 if the target was not in array, otherwise returns position
    """
    if array[0] == target:
        return 0

    left = 0
    right = len(array) - 1

    while left <= right:

        mid_index = (right + left) // 2

        prev_to_mid_element = array[mid_index - 1]
        mid_element = array[mid_index]

        if mid_element == target and prev_to_mid_element < target:
            return mid_index
        elif mid_element < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1


def find_first_last_position_v3(integer_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integer_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    if len(integer_array) == 0:
        return [-1, -1]

    first_position = binary_search_first_occurrence(integer_array, target)

    if first_position == -1:
        return [-1, -1]

    last_position = first_position

    while (last_position + 1) < len(integer_array) and integer_array[(last_position + 1)] == target:
        last_position += 1

    return [first_position, last_position]


# Checking
if __name__ == "__main__":
    assert (find_first_last_position_v3([], 10) == [-1, -1])
    assert (find_first_last_position_v3(int_array, 10) == [-1, -1])
    assert (find_first_last_position_v3(int_array, 5) == [2, 6])
    assert (find_first_last_position_v3(int_array, 7) == [7, 7])
