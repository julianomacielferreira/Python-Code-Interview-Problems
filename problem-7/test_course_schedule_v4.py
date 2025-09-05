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

from course_schedule_v4 import bfs


class BFSTestCase(unittest.TestCase):
    def test_bfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

        start_node = 'A'
        expected_output = ['A', 'B', 'C', 'D', 'E', 'F']

        self.assertEqual(bfs(graph, start_node), expected_output)

    def test_bfs_disconnected_graph(self):
        graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }

        start_node = 'A'
        expected_output = ['A', 'B']

        self.assertEqual(bfs(graph, start_node), expected_output)

    def test_bfs_cyclic_graph(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }

        start_node = 'A'
        expected_output = ['A', 'B', 'C']

        self.assertEqual(bfs(graph, start_node), expected_output)


if __name__ == '__main__':
    unittest.main()
