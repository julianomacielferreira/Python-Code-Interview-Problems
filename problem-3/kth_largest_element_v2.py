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
import numpy as np
from data import int_array


def kth_largest_element_v2(integer_array, k):
    """
        Given an array of integers and an integer k, find the kth largest element.

        Params:
            integer_array (array): Ordered array
            k (int): Position to find the element

        Returns:
            -1 if the target was not in array, otherwise returns the element
    """
    if k <= 0 or k > len(integer_array):
        return -1

    _array_ = np.array(integer_array)

    for i in range(k - 2):
        _array_ = np.delete(_array_, np.where(_array_ == max(_array_)))

    return max(_array_)


if __name__ == "__main__":
    assert (kth_largest_element_v2(int_array, 4) == 6)
    assert (kth_largest_element_v2(int_array, 11) == -1)
