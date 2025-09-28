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
from collections import Counter


def contains_all(freq1, freq2):
    """
    Checks if the frequency of characters in `freq1` is sufficient to cover `freq2`.

    Args:
    freq1 (dict): Dictionary with the frequency of characters in the first string.
    freq2 (dict): Dictionary with the frequency of characters in the second string.

    Returns:
    bool: True if `freq1` has sufficient frequency to cover `freq2`, False otherwise.
    """
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True


def min_window(s, t):
    """
    Find the smallest window (substring) in `s` that contains all the characters of `t`.

    Args:
    s (str): String where the window will be searched.
    t (str): String containing the characters the window should contain.

    Returns:
    str: The smallest window in `s` that contains all the characters of `t`. If there is no such window, it returns an empty string.
    """
    n, m = len(s), len(t)

    if m > n or m == 0:
        return ""

    freq_t = Counter(t)

    shortest = " " * (n + 1)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            freq_s = Counter(sub)
            if contains_all(freq_s, freq_t) and length < len(shortest):
                shortest = sub

    return shortest if len(shortest) <= n else ""
