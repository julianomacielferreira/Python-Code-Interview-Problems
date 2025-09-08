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
import itertools

from kth_permutation_v1 import kth_permutation


class KthPermutationTestCase(unittest.TestCase):
    def test_small_n(self):
        n = 3
        k = 2

        result = kth_permutation(n, k)
        permutations = list(itertools.permutations(range(1, n + 1)))
        expected = ''.join(map(str, permutations[k - 1]))

        self.assertEqual(result, expected)
        self.assertEqual(kth_permutation(3, 2), '132')

    def test_first_permutation(self):
        n = 3
        k = 1

        self.assertEqual(kth_permutation(n, k), '123')

    def test_last_permutation(self):
        n = 3
        k = 6  # 3! = 6

        self.assertEqual(kth_permutation(n, k), '321')

    def test_k_out_of_range_low(self):
        n = 3
        k = 0

        with self.assertRaises(ValueError):
            kth_permutation(n, k)

    def test_k_out_of_range_high(self):
        n = 3
        k = 7  # beyond 3! = 6

        with self.assertRaises(ValueError):
            kth_permutation(n, k)

    def test_n_1(self):
        n = 1
        k = 1

        self.assertEqual(kth_permutation(n, k), '1')


if __name__ == '__main__':
    unittest.main()
