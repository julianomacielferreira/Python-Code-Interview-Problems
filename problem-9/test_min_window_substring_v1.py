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
import unittest

from min_window_substring_v1 import min_window


class MinWindowSubstringTestCase(unittest.TestCase):
    def test_min_window_substring_found(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(min_window(s, t), "BANC")

    def test_min_window_substring_not_found(self):
        s = "ABC"
        t = "DEFG"
        self.assertEqual(min_window(s, t), "")

    def test_min_window_substring_empty_t(self):
        s = "ABC"
        t = ""
        self.assertEqual(min_window(s, t), "")

    def test_min_window_substring_t_longer_than_s(self):
        s = "ABC"
        t = "ABCDE"
        self.assertEqual(min_window(s, t), "")

    def test_min_window_substring_single_character(self):
        s = "AAAA"
        t = "A"
        self.assertEqual(min_window(s, t), "A")


if __name__ == '__main__':
    unittest.main()
