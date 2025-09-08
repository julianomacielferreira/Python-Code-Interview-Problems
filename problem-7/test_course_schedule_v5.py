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

from course_schedule_v4 import course_schedule


class CourseScheduleTestCase(unittest.TestCase):
    def test_valid_ordering(self):
        n = 4
        prerequisites = [[0, 1], [1, 2], [2, 3]]
        result = course_schedule(n, prerequisites)
        self.assertEqual(len(result), n)
        # Check valid topological order (one possible order)
        self.assertTrue(result in [[3, 2, 1, 0], [0, 1, 2, 3]])

    def test_cycle_no_valid_order(self):
        n = 2
        prerequisites = [[0, 1], [1, 0]]
        result = course_schedule(n, prerequisites)
        self.assertEqual(result, [])

    def test_no_prerequisites(self):
        n = 3
        prerequisites = []
        result = course_schedule(n, prerequisites)
        # Any permutation of [0,1,2] is valid
        self.assertEqual(set(result), set([0, 1, 2]))

    def test_single_course_no_prereqs(self):
        n = 1
        prerequisites = []
        result = course_schedule(n, prerequisites)
        self.assertEqual(result, [0])

    def test_complex_valid_ordering(self):
        n = 5
        prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3]]
        result = course_schedule(n, prerequisites)
        self.assertEqual(len(result), n)

    def test_empty_input(self):
        n = 0
        prerequisites = []
        result = course_schedule(n, prerequisites)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
