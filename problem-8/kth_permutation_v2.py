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
import math


def kth_permutation(n, k):
    """
    Returns the k-th lexicographically ordered permutation of numbers from 1 to n.

    Args:
        n (int): The number of elements to permute (1 to n)
        k (int): The position of the permutation in lexicographically order (1-indexed)

    Returns:
        str: The k-th permutation as a string of concatenated digits.

    Raises:
        ValueError: If k is out of range (k < 1 or k > n!).
    """
    if k < 1 or k > math.factorial(n):
        raise ValueError(f"k={k} out of range for n={n} (1 to {math.factorial(n)})")

    nums = list(range(1, n + 1))
    result = []

    k -= 1  # Adjust k to 0-indexed

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        k %= fact
        result.append(nums[index])
        nums.pop()

    return ''.join(map(str, result))
