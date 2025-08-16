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


def find_first_last_position(integers_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integers_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    is_target_in_array = False

    for i in range(len(integers_array)):
        if integers_array[i] == target:
            is_target_in_array = True
            break

    if not is_target_in_array:
        return [-1, -1]

    first_position = False
    last_position = False

    for i in range(len(integers_array)):
        if integers_array[i] == target:
            if not first_position:
                first_position = i
            else:
                last_position = i

    # Only one occurrence of target
    if not last_position:
        last_position = first_position

    return [first_position, last_position]


# Checking
if __name__ == "__main__":
    assert (find_first_last_position(int_array, 10) == [-1, -1])
    assert (find_first_last_position(int_array, 5) == [2, 6])
    assert (find_first_last_position(int_array, 7) == [7, 7])
